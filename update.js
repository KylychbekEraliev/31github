db.studentInfo.insert({
  name: { firstName: "Aktan", lastName: "Doe" },
  class: 6,
  rollNo: 23,
  subjects: ["Maths", "Aktan", "English", "Chemistry"],
  attendance: {
    January: "90%",
    February: "85%",
    March: "98%"
  }
});

db.studentInfo.insert({
  name: { firstName: "Peter", lastName: "A" },
  rollNo: 24,
  subjects: ["Maths", "Physics", "Kyrgyz", "Chemistry"],
  attendance: {
    January: "97%",
    February: "99%",
    March: "100%"
  }
});

db.studentInfo.insert({
  name: { firstName: "Dave", lastName: "J" },
  rollNo: 27,
  subjects: ["Maths", "Physics", "English", "Chemistry"],
  attendance: {
    January: "87%",
    February: "99%",
    March: "100%"
  }
});
