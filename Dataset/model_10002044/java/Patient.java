





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String sex;
    private int telno;
    private String name;
    private String address;
    private int age;
    private int id;
    private int roomno;





    private List<Doctor> doctors;


    public Patient(
        String sex,        int telno,        String name,        String address,        int age,        int id,        int roomno    ) {
        this.sex = sex;
        this.telno = telno;
        this.name = name;
        this.address = address;
        this.age = age;
        this.id = id;
        this.roomno = roomno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String sex,        int telno,        String name,        String address,        int age,        int id,        int roomno        ArrayList<Doctor> doctors    ) {
        this.sex = sex;
        this.telno = telno;
        this.name = name;
        this.address = address;
        this.age = age;
        this.id = id;
        this.roomno = roomno;
        this.doctors = doctors;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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