import ClassRoom from './0-classroom';

export default function initializeRooms() {
  // return [ new ClassRoom(19), new ClassRoom(20), new ClassRoom(34) ]
  const roomSizes = [19, 20, 34];
  return roomSizes.map((size) => new ClassRoom(size));
}
