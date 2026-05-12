





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String checkInTime;
    private int attendanceID;
    private String checkOutTime;





    private Profile profile;


    public Attendance(
        String checkInTime,        int attendanceID,        String checkOutTime    ) {
        this.checkInTime = checkInTime;
        this.attendanceID = attendanceID;
        this.checkOutTime = checkOutTime;
    }


    public String getCheckintime() {
        return checkInTime;
    }

    public void setCheckintime(String checkInTime) {
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

    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }

}