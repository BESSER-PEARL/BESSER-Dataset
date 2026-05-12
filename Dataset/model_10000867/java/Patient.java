





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int age;
    private String sex;
    private String name;
    private int roomno;
    private int id;
    private int telno;
    private String address;





    private List<Doctor> doctors;


    public Patient(
        int age,        String sex,        String name,        int roomno,        int id,        int telno,        String address    ) {
        this.age = age;
        this.sex = sex;
        this.name = name;
        this.roomno = roomno;
        this.id = id;
        this.telno = telno;
        this.address = address;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int age,        String sex,        String name,        int roomno,        int id,        int telno,        String address        ArrayList<Doctor> doctors    ) {
        this.age = age;
        this.sex = sex;
        this.name = name;
        this.roomno = roomno;
        this.id = id;
        this.telno = telno;
        this.address = address;
        this.doctors = doctors;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}