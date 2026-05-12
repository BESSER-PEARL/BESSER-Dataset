





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private int attendanceID;
    private String checkOutTime;
    private String checkInTime;



    public Attendance(
        int attendanceID,        String checkOutTime,        String checkInTime    ) {
        this.attendanceID = attendanceID;
        this.checkOutTime = checkOutTime;
        this.checkInTime = checkInTime;
    }


    public int getAttendanceid() {
        return attendanceID;
    }

    public void setAttendanceid(int attendanceID) {
        this.attendanceID = attendanceID;
    }
    public String getCheckouttime() {
        return checkOutTime;
    }

    public void setCheckouttime(String checkOutTime) {
        this.checkOutTime = checkOutTime;
    }
    public String getCheckintime() {
        return checkInTime;
    }

    public void setCheckintime(String checkInTime) {
        this.checkInTime = checkInTime;
    }


}