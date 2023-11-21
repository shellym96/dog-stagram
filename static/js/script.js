/* jshint esversion: 11, jquery: true */

// ensure dog's DOB is not in the future
let now = new Date(),
minDate = now.toISOString().substring(0,10);
$("#id_dob").prop("max", minDate);
