





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String address;
    private String name;
    private int age;
    private int telno;
    private String sex;
    private int id;





    private List<Doctor> doctors;


    public Patient(
        String address,        String name,        int age,        int telno,        String sex,        int id    ) {
        this.address = address;
        this.name = name;
        this.age = age;
        this.telno = telno;
        this.sex = sex;
        this.id = id;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String address,        String name,        int age,        int telno,        String sex,        int id        ArrayList<Doctor> doctors    ) {
        this.address = address;
        this.name = name;
        this.age = age;
        this.telno = telno;
        this.sex = sex;
        this.id = id;
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
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}