function bulkRefuel()
for s=16,1,-1 do
turtle.select(s)
if turtle.refuel() == true then turtle.refuel()
end
end
print("Done")
io.write("Current fuel level:")
print(turtle.getFuelLevel())
 
end
 
function preciseRefuel()
 
io.write("Fuel slot : ")
local slot = io.read()
 
io.write("Fuel level : ")
local level = io.read()
 
while turtle.getFuelLevel() < tonumber(level)
 and turtle.getItemCount(tonumber(slot)) > 0 do
 turtle.select(tonumber(slot))
 turtle.refuel(1)
 end
 
 if turtle.getItemCount(tonumber(slot)) == 0 then
 print("Not enough fuel")
 io.write("Current fuel level:")
 print(turtle.getFuelLevel())
 else print("Success!")
 end
  end
 
  function main()
  print("SuperRefuel - Rocky 2018")
 
  local i = 0
 
  io.write("PreciseRefuel(1) or BulkRefuel(2)?")
  while i == 0 do
  i = 1
  local mode = io.read()
  if tonumber(mode) == 1 then preciseRefuel()
  else if tonumber(mode) == 2 then bulkRefuel()
  else  print("Invalid mode")
  i = 0
  end
end
end
end
 
main()
