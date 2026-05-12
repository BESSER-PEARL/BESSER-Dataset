





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int telno;
    private String address;
    private int roomno;
    private int age;
    private int id;
    private String sex;
    private String name;





    private List<Doctor> doctors;


    public Patient(
        int telno,        String address,        int roomno,        int age,        int id,        String sex,        String name    ) {
        this.telno = telno;
        this.address = address;
        this.roomno = roomno;
        this.age = age;
        this.id = id;
        this.sex = sex;
        this.name = name;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int telno,        String address,        int roomno,        int age,        int id,        String sex,        String name        ArrayList<Doctor> doctors    ) {
        this.telno = telno;
        this.address = address;
        this.roomno = roomno;
        this.age = age;
        this.id = id;
        this.sex = sex;
        this.name = name;
        this.doctors = doctors;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}