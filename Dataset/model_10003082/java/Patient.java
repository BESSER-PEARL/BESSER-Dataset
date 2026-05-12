





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String sex;
    private int roomno;
    private int telno;
    private String address;
    private String name;
    private int age;
    private int id;



    public Patient(
        String sex,        int roomno,        int telno,        String address,        String name,        int age,        int id    ) {
        this.sex = sex;
        this.roomno = roomno;
        this.telno = telno;
        this.address = address;
        this.name = name;
        this.age = age;
        this.id = id;
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


}