const input = require("fs").readFileSync("stdin", "utf8");
const lines = input.split("\n")[0].split(" ");

const totalHoursInDay = 24;
const totalMinutesInHour = 60;
const totalMinutesInDay = totalHoursInDay * totalMinutesInHour;

const initialHour = Number(lines[0]);
const initialMinute = Number(lines[1]);
const finishHour = Number(lines[2]);
const finishMinute = Number(lines[3]);

const initialTotalMinutes = initialHour * totalMinutesInHour + initialMinute;
const finishTotalMinutes = finishHour * totalMinutesInHour + finishMinute;

let diff;
let diffHours;
let diffMinutes;

if (initialTotalMinutes === finishTotalMinutes) {
  diffHours = 24;
  diffMinutes = 0;
}

if (initialTotalMinutes > finishTotalMinutes) {
  diff = totalMinutesInDay - initialTotalMinutes + finishTotalMinutes;
  diffHours = parseInt(diff / totalMinutesInHour);
  diffMinutes = parseInt(diff % totalMinutesInHour);
}

if (initialTotalMinutes < finishTotalMinutes) {
  diff = finishTotalMinutes - initialTotalMinutes;
  diffHours = parseInt(diff / totalMinutesInHour);
  diffMinutes = parseInt(diff % totalMinutesInHour);
}

console.log(`O JOGO DUROU ${diffHours} HORA(S) E ${diffMinutes} MINUTO(S)`);
