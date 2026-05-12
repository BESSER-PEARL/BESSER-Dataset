





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Email;
    private String DoctorName;
    private String Speciality;
    private String DateOfBirth;
    private String DId;
    private int DoctorId;
    private int UserId;
    private String PhoneNumber;





    private List<Appointment> appointments;


    public Doctor(
        String Email,        String DoctorName,        String Speciality,        String DateOfBirth,        String DId,        int DoctorId,        int UserId,        String PhoneNumber    ) {
        this.Email = Email;
        this.DoctorName = DoctorName;
        this.Speciality = Speciality;
        this.DateOfBirth = DateOfBirth;
        this.DId = DId;
        this.DoctorId = DoctorId;
        this.UserId = UserId;
        this.PhoneNumber = PhoneNumber;
        this.appointments = new ArrayList<>();
    }

    public Doctor(
        String Email,        String DoctorName,        String Speciality,        String DateOfBirth,        String DId,        int DoctorId,        int UserId,        String PhoneNumber        ArrayList<Appointment> appointments    ) {
        this.Email = Email;
        this.DoctorName = DoctorName;
        this.Speciality = Speciality;
        this.DateOfBirth = DateOfBirth;
        this.DId = DId;
        this.DoctorId = DoctorId;
        this.UserId = UserId;
        this.PhoneNumber = PhoneNumber;
        this.appointments = appointments;
    }

    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getDoctorname() {
        return DoctorName;
    }

    public void setDoctorname(String DoctorName) {
        this.DoctorName = DoctorName;
    }
    public String getSpeciality() {
        return Speciality;
    }

    public void setSpeciality(String Speciality) {
        this.Speciality = Speciality;
    }
    public String getDateofbirth() {
        return DateOfBirth;
    }

    public void setDateofbirth(String DateOfBirth) {
        this.DateOfBirth = DateOfBirth;
    }
    public String getDid() {
        return DId;
    }

    public void setDid(String DId) {
        this.DId = DId;
    }
    public int getDoctorid() {
        return DoctorId;
    }

    public void setDoctorid(int DoctorId) {
        this.DoctorId = DoctorId;
    }
    public int getUserid() {
        return UserId;
    }

    public void setUserid(int UserId) {
        this.UserId = UserId;
    }
    public String getPhonenumber() {
        return PhoneNumber;
    }

    public void setPhonenumber(String PhoneNumber) {
        this.PhoneNumber = PhoneNumber;
    }

    public List<Appointment> getAppointments() {
        return appointments;
    }

    public void addAppointment(Appointment appointment) {
        this.appointments.add(appointment);
    }

}