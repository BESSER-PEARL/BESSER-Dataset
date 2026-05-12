





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int roomno;
    private String address;
    private int age;
    private String sex;
    private int telno;
    private String name;
    private int id;





    private List<Doctor> doctors;


    public Patient(
        int roomno,        String address,        int age,        String sex,        int telno,        String name,        int id    ) {
        this.roomno = roomno;
        this.address = address;
        this.age = age;
        this.sex = sex;
        this.telno = telno;
        this.name = name;
        this.id = id;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int roomno,        String address,        int age,        String sex,        int telno,        String name,        int id        ArrayList<Doctor> doctors    ) {
        this.roomno = roomno;
        this.address = address;
        this.age = age;
        this.sex = sex;
        this.telno = telno;
        this.name = name;
        this.id = id;
        this.doctors = doctors;
    }

    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}