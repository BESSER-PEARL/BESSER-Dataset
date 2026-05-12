





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String name;
    private int telno;
    private String address;
    private int roomno;
    private String sex;
    private int id;
    private int age;





    private List<Doctor> doctors;


    public Patient(
        String name,        int telno,        String address,        int roomno,        String sex,        int id,        int age    ) {
        this.name = name;
        this.telno = telno;
        this.address = address;
        this.roomno = roomno;
        this.sex = sex;
        this.id = id;
        this.age = age;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String name,        int telno,        String address,        int roomno,        String sex,        int id,        int age        ArrayList<Doctor> doctors    ) {
        this.name = name;
        this.telno = telno;
        this.address = address;
        this.roomno = roomno;
        this.sex = sex;
        this.id = id;
        this.age = age;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}