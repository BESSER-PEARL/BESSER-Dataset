





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int roomno;
    private int age;
    private int id;
    private int telno;
    private String name;
    private String address;
    private String sex;





    private List<Doctor> doctors;


    public Patient(
        int roomno,        int age,        int id,        int telno,        String name,        String address,        String sex    ) {
        this.roomno = roomno;
        this.age = age;
        this.id = id;
        this.telno = telno;
        this.name = name;
        this.address = address;
        this.sex = sex;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int roomno,        int age,        int id,        int telno,        String name,        String address,        String sex        ArrayList<Doctor> doctors    ) {
        this.roomno = roomno;
        this.age = age;
        this.id = id;
        this.telno = telno;
        this.name = name;
        this.address = address;
        this.sex = sex;
        this.doctors = doctors;
    }

    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getTelno() {
        return telno;
    }

    public void setTelno(int telno) {
        this.telno = telno;
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