





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private int attendanceID;
    private String checkInTime;
    private String checkOutTime;





    private Profile profile;


    public Attendance(
        int attendanceID,        String checkInTime,        String checkOutTime    ) {
        this.attendanceID = attendanceID;
        this.checkInTime = checkInTime;
        this.checkOutTime = checkOutTime;
    }


    public int getAttendanceid() {
        return attendanceID;
    }

    public void setAttendanceid(int attendanceID) {
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

    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }

}