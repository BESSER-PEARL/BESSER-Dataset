





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String checkInTime;
    private String checkOutTime;
    private int attendanceID;





    private Profile profile;


    public Attendance(
        String checkInTime,        String checkOutTime,        int attendanceID    ) {
        this.checkInTime = checkInTime;
        this.checkOutTime = checkOutTime;
        this.attendanceID = attendanceID;
    }


    public String getCheckintime() {
        return checkInTime;
    }

    public void setCheckintime(String checkInTime) {
        this.checkInTime = checkInTime;
    }
    public String getCheckouttime() {
        return checkOutTime;
    }

    public void setCheckouttime(String checkOutTime) {
        this.checkOutTime = checkOutTime;
    }
    public int getAttendanceid() {
        return attendanceID;
    }

    public void setAttendanceid(int attendanceID) {
        this.attendanceID = attendanceID;
    }

    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }

}