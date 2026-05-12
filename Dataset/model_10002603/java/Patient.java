





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int id;
    private int telno;
    private int age;
    private String address;
    private String sex;
    private int roomno;
    private String name;





    private List<Doctor> doctors;


    public Patient(
        int id,        int telno,        int age,        String address,        String sex,        int roomno,        String name    ) {
        this.id = id;
        this.telno = telno;
        this.age = age;
        this.address = address;
        this.sex = sex;
        this.roomno = roomno;
        this.name = name;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int id,        int telno,        int age,        String address,        String sex,        int roomno,        String name        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.telno = telno;
        this.age = age;
        this.address = address;
        this.sex = sex;
        this.roomno = roomno;
        this.name = name;
        this.doctors = doctors;
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
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}