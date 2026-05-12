





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private None gender;
    private int age;
    private String address;
    private String phone;



    public Person(
        None gender,        int age,        String address,        String phone    ) {
        this.gender = gender;
        this.age = age;
        this.address = address;
        this.phone = phone;
    }


    public None getGender() {
        return gender;
    }

    public void setGender(None gender) {
        this.gender = gender;
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
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }


}