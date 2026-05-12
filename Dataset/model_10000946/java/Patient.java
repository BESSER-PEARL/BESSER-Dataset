





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int roomno;
    private String sex;
    private int telno;
    private int age;
    private String address;
    private String name;
    private int id;





    private Bill bill;




    private Receptionist receptionist;




    private Room room;




    private List<Doctor> doctors;


    public Patient(
        int roomno,        String sex,        int telno,        int age,        String address,        String name,        int id    ) {
        this.roomno = roomno;
        this.sex = sex;
        this.telno = telno;
        this.age = age;
        this.address = address;
        this.name = name;
        this.id = id;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        int roomno,        String sex,        int telno,        int age,        String address,        String name,        int id        ArrayList<Doctor> doctors    ) {
        this.roomno = roomno;
        this.sex = sex;
        this.telno = telno;
        this.age = age;
        this.address = address;
        this.name = name;
        this.id = id;
        this.doctors = doctors;
    }

    public int getRoomno() {
        return roomno;
    }

    public void setRoomno(int roomno) {
        this.roomno = roomno;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
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

    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }
    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }
    public Room getRoom() {
        return room;
    }

    public void setRoom(Room room) {
        this.room = room;
    }
    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}