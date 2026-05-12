





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String sex;
    private int age;
    private String telno;
    private String name;
    private int id;
    private String address;
    private int roomno;





    private List<Doctor> doctors;




    private Bill bill;




    private Room room;




    private Receptionist receptionist;


    public Patient(
        String sex,        int age,        String telno,        String name,        int id,        String address,        int roomno    ) {
        this.sex = sex;
        this.age = age;
        this.telno = telno;
        this.name = name;
        this.id = id;
        this.address = address;
        this.roomno = roomno;
        this.doctors = new ArrayList<>();
    }

    public Patient(
        String sex,        int age,        String telno,        String name,        int id,        String address,        int roomno        ArrayList<Doctor> doctors    ) {
        this.sex = sex;
        this.age = age;
        this.telno = telno;
        this.name = name;
        this.id = id;
        this.address = address;
        this.roomno = roomno;
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
    public String getTelno() {
        return telno;
    }

    public void setTelno(String telno) {
        this.telno = telno;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }
    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }
    public Room getRoom() {
        return room;
    }

    public void setRoom(Room room) {
        this.room = room;
    }
    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }

}