





import java.util.List;
import java.util.ArrayList;

public class patient  {

    private String room_no;
    private String phone_no;
    private String pid;
    private String name;
    private String age;
    private String address;



    public patient(
        String room_no,        String phone_no,        String pid,        String name,        String age,        String address    ) {
        this.room_no = room_no;
        this.phone_no = phone_no;
        this.pid = pid;
        this.name = name;
        this.age = age;
        this.address = address;
    }


    public String getRoom_no() {
        return room_no;
    }

    public void setRoom_no(String room_no) {
        this.room_no = room_no;
    }
    public String getPhone_no() {
        return phone_no;
    }

    public void setPhone_no(String phone_no) {
        this.phone_no = phone_no;
    }
    public String getPid() {
        return pid;
    }

    public void setPid(String pid) {
        this.pid = pid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}