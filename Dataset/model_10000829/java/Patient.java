





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int age;
    private String name;
    private int id;
    private int telno;
    private String address;
    private String sex;





    private List<Doctor> doctors;


    public Patient(
        int age,        String name,        int id,        int telno,        String address,        String sex    ) {
        this.age = age;
        this.name = name;
        this.id = id;
        this.telno = telno;
        this.address = address;
        this.sex = sex;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int age,        String name,        int id,        int telno,        String address,        String sex        ArrayList<Doctor> doctors    ) {
        this.age = age;
        this.name = name;
        this.id = id;
        this.telno = telno;
        this.address = address;
        this.sex = sex;
        this.doctors = doctors;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
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
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}