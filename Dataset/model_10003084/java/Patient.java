





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int id;
    private String address;
    private String name;
    private String sex;
    private int roomno;
    private int age;
    private int telno;





    private List<Doctor> doctors;


    public Patient(
        int id,        String address,        String name,        String sex,        int roomno,        int age,        int telno    ) {
        this.id = id;
        this.address = address;
        this.name = name;
        this.sex = sex;
        this.roomno = roomno;
        this.age = age;
        this.telno = telno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int id,        String address,        String name,        String sex,        int roomno,        int age,        int telno        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.address = address;
        this.name = name;
        this.sex = sex;
        this.roomno = roomno;
        this.age = age;
        this.telno = telno;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}