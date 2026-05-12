





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int roomno;
    private int id;
    private String name;
    private String address;
    private int age;
    private String sex;
    private String telno;





    private List<Doctor> doctors;


    public Patient(
        int roomno,        int id,        String name,        String address,        int age,        String sex,        String telno    ) {
        this.roomno = roomno;
        this.id = id;
        this.name = name;
        this.address = address;
        this.age = age;
        this.sex = sex;
        this.telno = telno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int roomno,        int id,        String name,        String address,        int age,        String sex,        String telno        ArrayList<Doctor> doctors    ) {
        this.roomno = roomno;
        this.id = id;
        this.name = name;
        this.address = address;
        this.age = age;
        this.sex = sex;
        this.telno = telno;
        this.doctors = doctors;
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
    public String getTelno() {
        return telno;
    }

    public void setTelno(String telno) {
        this.telno = telno;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}