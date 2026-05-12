





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String address;
    private String name;
    private int id;
    private String sex;
    private int telno;
    private int age;
    private int roomno;





    private List<Doctor> doctors;


    public Patient(
        String address,        String name,        int id,        String sex,        int telno,        int age,        int roomno    ) {
        this.address = address;
        this.name = name;
        this.id = id;
        this.sex = sex;
        this.telno = telno;
        this.age = age;
        this.roomno = roomno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String address,        String name,        int id,        String sex,        int telno,        int age,        int roomno        ArrayList<Doctor> doctors    ) {
        this.address = address;
        this.name = name;
        this.id = id;
        this.sex = sex;
        this.telno = telno;
        this.age = age;
        this.roomno = roomno;
        this.doctors = doctors;
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