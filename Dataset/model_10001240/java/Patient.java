





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int age;
    private int roomno;
    private int id;
    private String address;
    private String sex;
    private String name;
    private int telno;





    private List<Doctor> doctors;


    public Patient(
        int age,        int roomno,        int id,        String address,        String sex,        String name,        int telno    ) {
        this.age = age;
        this.roomno = roomno;
        this.id = id;
        this.address = address;
        this.sex = sex;
        this.name = name;
        this.telno = telno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int age,        int roomno,        int id,        String address,        String sex,        String name,        int telno        ArrayList<Doctor> doctors    ) {
        this.age = age;
        this.roomno = roomno;
        this.id = id;
        this.address = address;
        this.sex = sex;
        this.name = name;
        this.telno = telno;
        this.doctors = doctors;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTelno() {
        return telno;
    }

    public void setTelno(int telno) {
        this.telno = telno;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}