





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String checkInTime;
    private None checkOutTime;
    private None attendanceID;





    private Profile profile;


    public Attendance(
        String checkInTime,        None checkOutTime,        None attendanceID    ) {
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
    public None getCheckouttime() {
        return checkOutTime;
    }

    public void setCheckouttime(None checkOutTime) {
        this.checkOutTime = checkOutTime;
    }
    public None getAttendanceid() {
        return attendanceID;
    }

    public void setAttendanceid(None attendanceID) {
        this.attendanceID = attendanceID;
    }

    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }

}