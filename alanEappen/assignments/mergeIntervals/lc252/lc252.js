// Problem Statement #

// Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.


//Given: intervals that represent 'N' appointments
//Goal: find if a person can attend all the appointments
//returning a boolean
/*
  start = interval[0].start
  end = interval[0].end
  sort the interals
  for loop with i pointing to the current element
  conditional
  if end >= current[i].start
  {
    if there was an overlapp which means he cant attend all appointments
    return false
  }
//if no overlap was found
return true 
edge cases{
  if interval.length == 0
  return null
}
*/
class Interval {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }

  print_interval() {
    process.stdout.write(`[${this.start}, ${this.end}]`);
  }
}

const can_attend_all_appointments = function (intervals) {
  if (intervals.length == 0) {
    return null
  }
  else if (intervals.length == 1) {
    return true
  }
  intervals.sort((a, b) => a.start - b.start);
  start = intervals[0].start
  end = intervals[0].end

  for (let i = 1; i < intervals.length; i++) {
    if (end >= intervals[i].start) {
      return false
    }
    else {
      start = intervals[i].start
      end = intervals[i].end
    }
  }
  return true;
};

/* Writing the solution again
const can_attend_all_appointments = function (intervals) {
  if (intervals.length == 0) {
    return null
  }
  else if (intervals.length == 1) {
    return true
  }
  intervals.sort((a, b) => a.start - b.start);
  start = intervals[0].start
  end = intervals[0].end

  for (let i = 1; i < intervals.length; i++) {
    if (end >= intervals[i].start) {
      return false
    }
    else {
      start = intervals[i].start
      end = intervals[i].end
    }
  }
  return true;
};
*/

console.log(`Can attend all appointments: ${can_attend_all_appointments([
  new Interval(1, 4),
  new Interval(2, 5),
  new Interval(7, 9),
])}`);

console.log(`Can attend all appointments: ${can_attend_all_appointments([
  new Interval(6, 7),
  new Interval(2, 4),
  new Interval(8, 12),
])}`);

console.log(`Can attend all appointments: ${can_attend_all_appointments([
  new Interval(4, 5),
  new Interval(2, 3),
  new Interval(3, 6),
])}`);

console.log(`Can attend all appointments: ${can_attend_all_appointments([
  new Interval(4, 5)
])}`);

console.log(`Can attend all appointments: ${can_attend_all_appointments([
])}`);





// Solution
// -----
// function can_attend_all_appointments(intervals) {
//   intervals.sort((a, b) => a.start - b.start);
//   for (i = 1; i < intervals.length; i++) {
//     if (intervals[i].start < intervals[i - 1].end) {
//       // please note the comparison above, it is "<" and not "<="
//       // while merging we needed "<=" comparison, as we will be merging the two
//       // intervals having condition "intervals[i][start] === intervals[i - 1][end]" but
//       // such intervals don't represent conflicting appointments as one starts right
//       // after the other
//       return false;
//     }
//   }
//   return true;
// }

// -----

// Time complexity #
// The time complexity of the above algorithm is O(N*logN), where ‘N’ is the total number of appointments. Though we are iterating the intervals only once, our algorithm will take O(N * logN) since we need to sort them in the beginning.

// Space complexity #
// The space complexity of the above algorithm will be O(N), which we need for sorting. For Java, Arrays.sort() uses Timsort, which needs O(N) space.
