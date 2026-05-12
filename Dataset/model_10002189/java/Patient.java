




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String sex;
    private LocalDate accepted;
    private String sickness;
    private int telno;
    private String address;
    private int roomno;
    private int age;





    private List<Doctor> doctors;


    public Patient(
        String sex,        LocalDate accepted,        String sickness,        int telno,        String address,        int roomno,        int age    ) {
        this.sex = sex;
        this.accepted = accepted;
        this.sickness = sickness;
        this.telno = telno;
        this.address = address;
        this.roomno = roomno;
        this.age = age;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String sex,        LocalDate accepted,        String sickness,        int telno,        String address,        int roomno,        int age        ArrayList<Doctor> doctors    ) {
        this.sex = sex;
        this.accepted = accepted;
        this.sickness = sickness;
        this.telno = telno;
        this.address = address;
        this.roomno = roomno;
        this.age = age;
        this.doctors = doctors;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public LocalDate getAccepted() {
        return accepted;
    }

    public void setAccepted(LocalDate accepted) {
        this.accepted = accepted;
    }
    public String getSickness() {
        return sickness;
    }

    public void setSickness(String sickness) {
        this.sickness = sickness;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}