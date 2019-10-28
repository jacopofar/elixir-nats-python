defmodule EnpelixirTest do
  use ExUnit.Case
  doctest Enpelixir

  test "greets the world" do
    assert Enpelixir.hello() == :world
  end
end
