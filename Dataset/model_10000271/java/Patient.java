





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String name;
    private String sex;
    private String address;
    private int id;
    private int telno;
    private int age;
    private int roomno;





    private List<Doctor> doctors;


    public Patient(
        String name,        String sex,        String address,        int id,        int telno,        int age,        int roomno    ) {
        this.name = name;
        this.sex = sex;
        this.address = address;
        this.id = id;
        this.telno = telno;
        this.age = age;
        this.roomno = roomno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String name,        String sex,        String address,        int id,        int telno,        int age,        int roomno        ArrayList<Doctor> doctors    ) {
        this.name = name;
        this.sex = sex;
        this.address = address;
        this.id = id;
        this.telno = telno;
        this.age = age;
        this.roomno = roomno;
        this.doctors = doctors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}