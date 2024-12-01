let str = "The_stealth-warrior"

function toCamelCase(str){
    let strList = str.split('')
    let output = [];
    for (let i = 0; i < strList.length; i++) {
        if (/[A-Za-z]/.test(strList[i])) {
            if (/[A-Za-z]/.test(strList[i - 1])) {
                output.push(strList[i]);
            } 
            else {
                output.push(strList[i].toUpperCase());
            }
        }
    }
    return output.join('');
}

console.log(toCamelCase(str))