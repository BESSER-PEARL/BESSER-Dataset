





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String address;
    private String name;
    private int roomno;
    private int telno;
    private int age;
    private String sex;
    private int id;





    private List<Doctor> doctors;


    public Patient(
        String address,        String name,        int roomno,        int telno,        int age,        String sex,        int id    ) {
        this.address = address;
        this.name = name;
        this.roomno = roomno;
        this.telno = telno;
        this.age = age;
        this.sex = sex;
        this.id = id;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String address,        String name,        int roomno,        int telno,        int age,        String sex,        int id        ArrayList<Doctor> doctors    ) {
        this.address = address;
        this.name = name;
        this.roomno = roomno;
        this.telno = telno;
        this.age = age;
        this.sex = sex;
        this.id = id;
        this.doctors = doctors;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
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
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
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