





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int age;
    private String name;
    private String address;
    private String sex;
    private int roomno;
    private int telno;
    private int id;



    public Patient(
        int age,        String name,        String address,        String sex,        int roomno,        int telno,        int id    ) {
        this.age = age;
        this.name = name;
        this.address = address;
        this.sex = sex;
        this.roomno = roomno;
        this.telno = telno;
        this.id = id;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}