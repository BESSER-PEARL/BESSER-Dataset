





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int roomno;
    private String address;
    private String sex;
    private int age;
    private String name;
    private int telno;
    private int id;





    private List<Doctor> doctors;


    public Patient(
        int roomno,        String address,        String sex,        int age,        String name,        int telno,        int id    ) {
        this.roomno = roomno;
        this.address = address;
        this.sex = sex;
        this.age = age;
        this.name = name;
        this.telno = telno;
        this.id = id;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int roomno,        String address,        String sex,        int age,        String name,        int telno,        int id        ArrayList<Doctor> doctors    ) {
        this.roomno = roomno;
        this.address = address;
        this.sex = sex;
        this.age = age;
        this.name = name;
        this.telno = telno;
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
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
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
    public int getTelno() {
        return telno;
    }

    public void setTelno(int telno) {
        this.telno = telno;
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