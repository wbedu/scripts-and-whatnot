#!/usr/bin/env node
/*
* comparing run time for
* array.concat VS array.forEach
* when building a new array
* Is it overcomplicated? yes
* is it accurate? I sure hope so
*/
const totalRounds = 5
const itemsPerRound = 10000000

function trial(length) {
  const arr = Array.from({ length }).fill(null);

  let dest = [];
  const forEachStart = new Date();
  arr.forEach(e => {
    dest.push(e);
  })
  const forEachStop = new Date();
  dest = [];

  const concatStart = new Date();
  dest = dest.concat(arr);
  const concatStop = new Date();

  return {
    forEachTime: forEachStop - forEachStart,
    concatTime: concatStop - concatStart,
  }
}

const rounds = Array.from(
  { length: 5 },
  (item, index) => item = index + 1,
);


const results = rounds.map(
  () => trial(itemsPerRound),
);

console.log(`Trail Results for ${totalRounds} Rounds, ${itemsPerRound} array length`)

console.table(results)

const averageConcatTime = results.reduce(
  (sum, round) => round.concatTime + sum
  , 0) / totalRounds;

const averageForEachTime = results.reduce(
  (sum, round) => round.forEachTime + sum
  , 0) / totalRounds;

console.log(`\nAverage Times\nforEach : ${averageForEachTime}\nconcat  : ${averageConcatTime}`)
const speedUp = averageForEachTime > averageConcatTime
                  ? averageForEachTime / averageConcatTime
                  : averageConcatTime / averageForEachTime;
console.log(`speed up: ${speedUp}`);
