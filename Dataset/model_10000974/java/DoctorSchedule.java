





import java.util.List;
import java.util.ArrayList;

public class DoctorSchedule  {

    private String AvailableTime;
    private int DSid;
    private String DoctorId;
    private String AvailableDate;





    private List<Doctor> doctors;


    public DoctorSchedule(
        String AvailableTime,        int DSid,        String DoctorId,        String AvailableDate    ) {
        this.AvailableTime = AvailableTime;
        this.DSid = DSid;
        this.DoctorId = DoctorId;
        this.AvailableDate = AvailableDate;
        this.doctors = new ArrayList<>();
    }

    public DoctorSchedule(
        String AvailableTime,        int DSid,        String DoctorId,        String AvailableDate        ArrayList<Doctor> doctors    ) {
        this.AvailableTime = AvailableTime;
        this.DSid = DSid;
        this.DoctorId = DoctorId;
        this.AvailableDate = AvailableDate;
        this.doctors = doctors;
    }

    public String getAvailabletime() {
        return AvailableTime;
    }

    public void setAvailabletime(String AvailableTime) {
        this.AvailableTime = AvailableTime;
    }
    public int getDsid() {
        return DSid;
    }

    public void setDsid(int DSid) {
        this.DSid = DSid;
    }
    public String getDoctorid() {
        return DoctorId;
    }

    public void setDoctorid(String DoctorId) {
        this.DoctorId = DoctorId;
    }
    public String getAvailabledate() {
        return AvailableDate;
    }

    public void setAvailabledate(String AvailableDate) {
        this.AvailableDate = AvailableDate;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}