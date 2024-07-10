// Update script.js

// MongoDB update operation
db.studentInfo.updateMany(
    {},
    {
        $set: {
            'attendance.November': '$unset: { "attendance.January": "" }'
        }
    }
);
