//solve https://stackoverflow.com/questions/64288401/first-index-wont-populate-correct-amount-of-times/64288700#64288700

const progress = (start, end, length) =>{
/**
 * Builds array for an arithmetic progression:
 * [Based on wiki](https://en.wikipedia.org/wiki/Arithmetic_progression).
 *
 * @param {number} start starting elemnt
 * @param {number} end	last to include in array
 * @param {number} length total elements in array
 */
	const step = (end-start)/length;
	return Array.from({length: length}, (v, i) => {
		return (i * step) + start
	});
}


let arr = progress(100, 10, 10);

arr.forEach(elem =>console.log(elem));
@wbedu
