export default function appendToEachArrayValue(array, appendString) {
  for (const word of array) {
    array[array.indexOf(word)] = appendString + word;
  }

  return array;
}
