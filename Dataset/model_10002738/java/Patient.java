





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int id;
    private int roomno;
    private String name;
    private int telno;
    private int age;
    private String address;
    private String sex;





    private Admin admin;




    private List<Doctor> doctors;


    public Patient(
        int id,        int roomno,        String name,        int telno,        int age,        String address,        String sex    ) {
        this.id = id;
        this.roomno = roomno;
        this.name = name;
        this.telno = telno;
        this.age = age;
        this.address = address;
        this.sex = sex;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int id,        int roomno,        String name,        int telno,        int age,        String address,        String sex        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.roomno = roomno;
        this.name = name;
        this.telno = telno;
        this.age = age;
        this.address = address;
        this.sex = sex;
        this.doctors = doctors;
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
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
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

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}