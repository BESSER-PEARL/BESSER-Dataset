





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int id;
    private String sex;
    private String name;
    private String address;
    private int telno;
    private int age;
    private int roomno;





    private Bill bill;




    private Receptionist receptionist;




    private List<Doctor> doctors;


    public Patient(
        int id,        String sex,        String name,        String address,        int telno,        int age,        int roomno    ) {
        this.id = id;
        this.sex = sex;
        this.name = name;
        this.address = address;
        this.telno = telno;
        this.age = age;
        this.roomno = roomno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int id,        String sex,        String name,        String address,        int telno,        int age,        int roomno        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.sex = sex;
        this.name = name;
        this.address = address;
        this.telno = telno;
        this.age = age;
        this.roomno = roomno;
        this.doctors = doctors;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getTelno() {
        return telno;
    }

    public void setTelno(int telno) {
        this.telno = telno;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }

    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }
    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }
    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}