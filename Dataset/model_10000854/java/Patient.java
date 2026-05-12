





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int telno;
    private int age;
    private int id;
    private String sex;
    private String name;
    private String address;
    private int roomno;





    private List<Doctor> doctors;


    public Patient(
        int telno,        int age,        int id,        String sex,        String name,        String address,        int roomno    ) {
        this.telno = telno;
        this.age = age;
        this.id = id;
        this.sex = sex;
        this.name = name;
        this.address = address;
        this.roomno = roomno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int telno,        int age,        int id,        String sex,        String name,        String address,        int roomno        ArrayList<Doctor> doctors    ) {
        this.telno = telno;
        this.age = age;
        this.id = id;
        this.sex = sex;
        this.name = name;
        this.address = address;
        this.roomno = roomno;
        this.doctors = doctors;
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