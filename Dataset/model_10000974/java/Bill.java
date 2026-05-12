





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String BillDate;
    private String BId;
    private int BillId;
    private String PatientName;
    private String DoctorName;
    private int TotalAmount;
    private int Did;
    private int PId;





    private List<Doctor> doctors;




    private List<Patient> patients;


    public Bill(
        String BillDate,        String BId,        int BillId,        String PatientName,        String DoctorName,        int TotalAmount,        int Did,        int PId    ) {
        this.BillDate = BillDate;
        this.BId = BId;
        this.BillId = BillId;
        this.PatientName = PatientName;
        this.DoctorName = DoctorName;
        this.TotalAmount = TotalAmount;
        this.Did = Did;
        this.PId = PId;
        this.doctors = new ArrayList<>();
        this.patients = new ArrayList<>();
    }

    public Bill(
        String BillDate,        String BId,        int BillId,        String PatientName,        String DoctorName,        int TotalAmount,        int Did,        int PId        ArrayList<Doctor> doctors,        ArrayList<Patient> patients    ) {
        this.BillDate = BillDate;
        this.BId = BId;
        this.BillId = BillId;
        this.PatientName = PatientName;
        this.DoctorName = DoctorName;
        this.TotalAmount = TotalAmount;
        this.Did = Did;
        this.PId = PId;
        this.doctors = doctors;
        this.patients = patients;
    }

    public String getBilldate() {
        return BillDate;
    }

    public void setBilldate(String BillDate) {
        this.BillDate = BillDate;
    }
    public String getBid() {
        return BId;
    }

    public void setBid(String BId) {
        this.BId = BId;
    }
    public int getBillid() {
        return BillId;
    }

    public void setBillid(int BillId) {
        this.BillId = BillId;
    }
    public String getPatientname() {
        return PatientName;
    }

    public void setPatientname(String PatientName) {
        this.PatientName = PatientName;
    }
    public String getDoctorname() {
        return DoctorName;
    }

    public void setDoctorname(String DoctorName) {
        this.DoctorName = DoctorName;
    }
    public int getTotalamount() {
        return TotalAmount;
    }

    public void setTotalamount(int TotalAmount) {
        this.TotalAmount = TotalAmount;
    }
    public int getDid() {
        return Did;
    }

    public void setDid(int Did) {
        this.Did = Did;
    }
    public int getPid() {
        return PId;
    }

    public void setPid(int PId) {
        this.PId = PId;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }
    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}