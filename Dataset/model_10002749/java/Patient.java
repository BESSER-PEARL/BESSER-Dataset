





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int id;
    private String sex;
    private String address;
    private int roomno;
    private String name;
    private int telno;
    private int age;





    private List<Doctor> doctors;


    public Patient(
        int id,        String sex,        String address,        int roomno,        String name,        int telno,        int age    ) {
        this.id = id;
        this.sex = sex;
        this.address = address;
        this.roomno = roomno;
        this.name = name;
        this.telno = telno;
        this.age = age;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int id,        String sex,        String address,        int roomno,        String name,        int telno,        int age        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.sex = sex;
        this.address = address;
        this.roomno = roomno;
        this.name = name;
        this.telno = telno;
        this.age = age;
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