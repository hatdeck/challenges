/* If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Return the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
*/

function solution(number){
  if (number < 0){
    return 0
  }
  let arr = Array.from({length: number}, (v, i) => i)
  let res = new Array()
  arr.forEach(v => {
    if (v % 15 == 0) {
      res.push(v)
    } else if (v % 5 == 0) {
      res.push(v)
    } else if (v % 3 == 0) {
      res.push(v)
    }
  })
  return res.reduce((a, v) => a + v, 0)

}
