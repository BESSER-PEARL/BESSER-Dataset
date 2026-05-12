





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String address;
    private String sex;
    private int id;
    private int roomno;
    private int age;
    private int telno;
    private String name;





    private List<Doctor> doctors;


    public Patient(
        String address,        String sex,        int id,        int roomno,        int age,        int telno,        String name    ) {
        this.address = address;
        this.sex = sex;
        this.id = id;
        this.roomno = roomno;
        this.age = age;
        this.telno = telno;
        this.name = name;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String address,        String sex,        int id,        int roomno,        int age,        int telno,        String name        ArrayList<Doctor> doctors    ) {
        this.address = address;
        this.sex = sex;
        this.id = id;
        this.roomno = roomno;
        this.age = age;
        this.telno = telno;
        this.name = name;
        this.doctors = doctors;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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