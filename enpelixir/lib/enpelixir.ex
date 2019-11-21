defmodule Enpelixir do
  use Application

  @moduledoc """
  Documentation for Enpelixir.
  """

  @doc """
  Hello world.

  ## Examples

      iex> Enpelixir.hello()
      :world

  """
  def start(_type, _args) do
    IO.puts("starting")
    {:ok, gnat} = Gnat.start_link(%{host: '127.0.0.1', port: 4222})
    {:ok, _subscription} = Gnat.sub(gnat, self(), "*")
    IO.puts("Connected and subscribed")
    hello(gnat)
    IO.puts("application concluded!")
    # this is because Elixir wants a supervision tree to be returned
    Supervisor.start_link([], strategy: :one_for_one)
  end

  def hello(gnat) do
    receive do
        {:msg, %{body: body, topic: "test-subject", reply_to: nil}} ->
        IO.puts("Received: #{body}")
        if :rand.uniform() > 0.5 do
            IO.puts("Will send a message now...")
            :ok = Gnat.pub(gnat, "test-subject-two", "Hello snake-y friend, this is Elixir writing!")
        end
    end
    hello(gnat)
  end
end
