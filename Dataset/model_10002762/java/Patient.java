





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int telno;
    private int roomno;
    private int id;
    private String name;
    private int age;
    private String address;
    private String sex;





    private List<Doctor> doctors;


    public Patient(
        int telno,        int roomno,        int id,        String name,        int age,        String address,        String sex    ) {
        this.telno = telno;
        this.roomno = roomno;
        this.id = id;
        this.name = name;
        this.age = age;
        this.address = address;
        this.sex = sex;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int telno,        int roomno,        int id,        String name,        int age,        String address,        String sex        ArrayList<Doctor> doctors    ) {
        this.telno = telno;
        this.roomno = roomno;
        this.id = id;
        this.name = name;
        this.age = age;
        this.address = address;
        this.sex = sex;
        this.doctors = doctors;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}