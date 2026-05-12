





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int id;
    private int age;
    private String name;
    private String address;
    private int telno;
    private int roomno;
    private String sex;





    private List<Doctor> doctors;


    public Patient(
        int id,        int age,        String name,        String address,        int telno,        int roomno,        String sex    ) {
        this.id = id;
        this.age = age;
        this.name = name;
        this.address = address;
        this.telno = telno;
        this.roomno = roomno;
        this.sex = sex;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int id,        int age,        String name,        String address,        int telno,        int roomno,        String sex        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.age = age;
        this.name = name;
        this.address = address;
        this.telno = telno;
        this.roomno = roomno;
        this.sex = sex;
        this.doctors = doctors;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
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
    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}