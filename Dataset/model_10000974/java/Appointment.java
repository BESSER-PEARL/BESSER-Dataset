





import java.util.List;
import java.util.ArrayList;

public class Appointment  {

    private int Did;
    private String AppointmentDate;
    private String PatientName;
    private String Aid;
    private int PatientId;
    private String Reason;
    private int ServiceId;
    private int AppointmentId;
    private String AppointmentStatus;
    private String DoctorName;
    private String AppointmentTime;





    private List<Patient> patients;


    public Appointment(
        int Did,        String AppointmentDate,        String PatientName,        String Aid,        int PatientId,        String Reason,        int ServiceId,        int AppointmentId,        String AppointmentStatus,        String DoctorName,        String AppointmentTime    ) {
        this.Did = Did;
        this.AppointmentDate = AppointmentDate;
        this.PatientName = PatientName;
        this.Aid = Aid;
        this.PatientId = PatientId;
        this.Reason = Reason;
        this.ServiceId = ServiceId;
        this.AppointmentId = AppointmentId;
        this.AppointmentStatus = AppointmentStatus;
        this.DoctorName = DoctorName;
        this.AppointmentTime = AppointmentTime;
        this.patients = new ArrayList<>();
    }

    public Appointment(
        int Did,        String AppointmentDate,        String PatientName,        String Aid,        int PatientId,        String Reason,        int ServiceId,        int AppointmentId,        String AppointmentStatus,        String DoctorName,        String AppointmentTime        ArrayList<Patient> patients    ) {
        this.Did = Did;
        this.AppointmentDate = AppointmentDate;
        this.PatientName = PatientName;
        this.Aid = Aid;
        this.PatientId = PatientId;
        this.Reason = Reason;
        this.ServiceId = ServiceId;
        this.AppointmentId = AppointmentId;
        this.AppointmentStatus = AppointmentStatus;
        this.DoctorName = DoctorName;
        this.AppointmentTime = AppointmentTime;
        this.patients = patients;
    }

    public int getDid() {
        return Did;
    }

    public void setDid(int Did) {
        this.Did = Did;
    }
    public String getAppointmentdate() {
        return AppointmentDate;
    }

    public void setAppointmentdate(String AppointmentDate) {
        this.AppointmentDate = AppointmentDate;
    }
    public String getPatientname() {
        return PatientName;
    }

    public void setPatientname(String PatientName) {
        this.PatientName = PatientName;
    }
    public String getAid() {
        return Aid;
    }

    public void setAid(String Aid) {
        this.Aid = Aid;
    }
    public int getPatientid() {
        return PatientId;
    }

    public void setPatientid(int PatientId) {
        this.PatientId = PatientId;
    }
    public String getReason() {
        return Reason;
    }

    public void setReason(String Reason) {
        this.Reason = Reason;
    }
    public int getServiceid() {
        return ServiceId;
    }

    public void setServiceid(int ServiceId) {
        this.ServiceId = ServiceId;
    }
    public int getAppointmentid() {
        return AppointmentId;
    }

    public void setAppointmentid(int AppointmentId) {
        this.AppointmentId = AppointmentId;
    }
    public String getAppointmentstatus() {
        return AppointmentStatus;
    }

    public void setAppointmentstatus(String AppointmentStatus) {
        this.AppointmentStatus = AppointmentStatus;
    }
    public String getDoctorname() {
        return DoctorName;
    }

    public void setDoctorname(String DoctorName) {
        this.DoctorName = DoctorName;
    }
    public String getAppointmenttime() {
        return AppointmentTime;
    }

    public void setAppointmenttime(String AppointmentTime) {
        this.AppointmentTime = AppointmentTime;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}