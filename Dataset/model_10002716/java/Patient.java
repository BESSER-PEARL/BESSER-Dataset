





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int id;
    private int roomno;
    private int telno;
    private String address;
    private String name;
    private int age;
    private String sex;





    private List<Doctor> doctors;


    public Patient(
        int id,        int roomno,        int telno,        String address,        String name,        int age,        String sex    ) {
        this.id = id;
        this.roomno = roomno;
        this.telno = telno;
        this.address = address;
        this.name = name;
        this.age = age;
        this.sex = sex;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int id,        int roomno,        int telno,        String address,        String name,        int age,        String sex        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.roomno = roomno;
        this.telno = telno;
        this.address = address;
        this.name = name;
        this.age = age;
        this.sex = sex;
        this.doctors = doctors;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}