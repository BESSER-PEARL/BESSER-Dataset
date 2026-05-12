




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String sex;
    private int age;
    private String address;
    private LocalDate accepted;
    private String sickness;
    private int roomno;
    private int telno;





    private List<Doctor> doctors;


    public Patient(
        String sex,        int age,        String address,        LocalDate accepted,        String sickness,        int roomno,        int telno    ) {
        this.sex = sex;
        this.age = age;
        this.address = address;
        this.accepted = accepted;
        this.sickness = sickness;
        this.roomno = roomno;
        this.telno = telno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String sex,        int age,        String address,        LocalDate accepted,        String sickness,        int roomno,        int telno        ArrayList<Doctor> doctors    ) {
        this.sex = sex;
        this.age = age;
        this.address = address;
        this.accepted = accepted;
        this.sickness = sickness;
        this.roomno = roomno;
        this.telno = telno;
        this.doctors = doctors;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
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
    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
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