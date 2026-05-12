





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int id;
    private String sex;
    private int age;
    private String address;
    private int roomno;
    private int telno;
    private String name;





    private List<Doctor> doctors;


    public Patient(
        int id,        String sex,        int age,        String address,        int roomno,        int telno,        String name    ) {
        this.id = id;
        this.sex = sex;
        this.age = age;
        this.address = address;
        this.roomno = roomno;
        this.telno = telno;
        this.name = name;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int id,        String sex,        int age,        String address,        int roomno,        int telno,        String name        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.sex = sex;
        this.age = age;
        this.address = address;
        this.roomno = roomno;
        this.telno = telno;
        this.name = name;
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
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}