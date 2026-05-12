





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String sex;
    private String name;
    private int age;
    private int id;
    private String address;
    private int telno;





    private List<Doctor> doctors;


    public Patient(
        String sex,        String name,        int age,        int id,        String address,        int telno    ) {
        this.sex = sex;
        this.name = name;
        this.age = age;
        this.id = id;
        this.address = address;
        this.telno = telno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String sex,        String name,        int age,        int id,        String address,        int telno        ArrayList<Doctor> doctors    ) {
        this.sex = sex;
        this.name = name;
        this.age = age;
        this.id = id;
        this.address = address;
        this.telno = telno;
        this.doctors = doctors;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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