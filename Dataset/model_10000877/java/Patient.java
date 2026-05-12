





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String name;
    private int telno;
    private int roomno;
    private int age;
    private String sex;
    private String address;
    private int id;





    private List<Doctor> doctors;


    public Patient(
        String name,        int telno,        int roomno,        int age,        String sex,        String address,        int id    ) {
        this.name = name;
        this.telno = telno;
        this.roomno = roomno;
        this.age = age;
        this.sex = sex;
        this.address = address;
        this.id = id;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String name,        int telno,        int roomno,        int age,        String sex,        String address,        int id        ArrayList<Doctor> doctors    ) {
        this.name = name;
        this.telno = telno;
        this.roomno = roomno;
        this.age = age;
        this.sex = sex;
        this.address = address;
        this.id = id;
        this.doctors = doctors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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