





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int age;
    private int telno;
    private String address;
    private int id;
    private String name;
    private String sex;
    private int roomno;





    private List<Doctor> doctors;


    public Patient(
        int age,        int telno,        String address,        int id,        String name,        String sex,        int roomno    ) {
        this.age = age;
        this.telno = telno;
        this.address = address;
        this.id = id;
        this.name = name;
        this.sex = sex;
        this.roomno = roomno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int age,        int telno,        String address,        int id,        String name,        String sex,        int roomno        ArrayList<Doctor> doctors    ) {
        this.age = age;
        this.telno = telno;
        this.address = address;
        this.id = id;
        this.name = name;
        this.sex = sex;
        this.roomno = roomno;
        this.doctors = doctors;
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