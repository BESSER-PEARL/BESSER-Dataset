





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String Sex;
    private int RoomNo;
    private int PatientID;
    private String TelephoneNo;
    private String Address;
    private String Name;
    private int Age;





    private Bill bill;




    private List<Doctor> doctors;


    public Patient(
        String Sex,        int RoomNo,        int PatientID,        String TelephoneNo,        String Address,        String Name,        int Age    ) {
        this.Sex = Sex;
        this.RoomNo = RoomNo;
        this.PatientID = PatientID;
        this.TelephoneNo = TelephoneNo;
        this.Address = Address;
        this.Name = Name;
        this.Age = Age;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String Sex,        int RoomNo,        int PatientID,        String TelephoneNo,        String Address,        String Name,        int Age        ArrayList<Doctor> doctors    ) {
        this.Sex = Sex;
        this.RoomNo = RoomNo;
        this.PatientID = PatientID;
        this.TelephoneNo = TelephoneNo;
        this.Address = Address;
        this.Name = Name;
        this.Age = Age;
        this.doctors = doctors;
    }

    public String getSex() {
        return Sex;
    }

    public void setSex(String Sex) {
        this.Sex = Sex;
    }
    public int getRoomno() {
        return RoomNo;
    }

    public void setRoomno(int RoomNo) {
        this.RoomNo = RoomNo;
    }
    public int getPatientid() {
        return PatientID;
    }

    public void setPatientid(int PatientID) {
        this.PatientID = PatientID;
    }
    public String getTelephoneno() {
        return TelephoneNo;
    }

    public void setTelephoneno(String TelephoneNo) {
        this.TelephoneNo = TelephoneNo;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }

    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }
    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}