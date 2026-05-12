




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int age;
    private LocalDate accepted;
    private int roomno;
    private String sickness;
    private String sex;
    private String address;
    private int telno;





    private List<Doctor> doctors;


    public Patient(
        int age,        LocalDate accepted,        int roomno,        String sickness,        String sex,        String address,        int telno    ) {
        this.age = age;
        this.accepted = accepted;
        this.roomno = roomno;
        this.sickness = sickness;
        this.sex = sex;
        this.address = address;
        this.telno = telno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int age,        LocalDate accepted,        int roomno,        String sickness,        String sex,        String address,        int telno        ArrayList<Doctor> doctors    ) {
        this.age = age;
        this.accepted = accepted;
        this.roomno = roomno;
        this.sickness = sickness;
        this.sex = sex;
        this.address = address;
        this.telno = telno;
        this.doctors = doctors;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public LocalDate getAccepted() {
        return accepted;
    }

    public void setAccepted(LocalDate accepted) {
        this.accepted = accepted;
    }
    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }
    public String getSickness() {
        return sickness;
    }

    public void setSickness(String sickness) {
        this.sickness = sickness;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
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