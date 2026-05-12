





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String phoneNumber;
    private String gender;
    private String name;
    private String address;
    private String title;



    public Person(
        String phoneNumber,        String gender,        String name,        String address,        String title    ) {
        this.phoneNumber = phoneNumber;
        this.gender = gender;
        this.name = name;
        this.address = address;
        this.title = title;
    }


    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}