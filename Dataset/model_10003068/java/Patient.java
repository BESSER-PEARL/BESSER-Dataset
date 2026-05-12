





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int id;
    private String address;
    private int age;
    private String sex;
    private String name;
    private int telno;
    private int roomno;





    private List<Doctor> doctors;


    public Patient(
        int id,        String address,        int age,        String sex,        String name,        int telno,        int roomno    ) {
        this.id = id;
        this.address = address;
        this.age = age;
        this.sex = sex;
        this.name = name;
        this.telno = telno;
        this.roomno = roomno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int id,        String address,        int age,        String sex,        String name,        int telno,        int roomno        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.address = address;
        this.age = age;
        this.sex = sex;
        this.name = name;
        this.telno = telno;
        this.roomno = roomno;
        this.doctors = doctors;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}