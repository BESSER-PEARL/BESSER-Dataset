





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String phone;
    private int age;
    private String address;



    public Patient(
        String phone,        int age,        String address    ) {
        this.phone = phone;
        this.age = age;
        this.address = address;
    }


    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
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


}