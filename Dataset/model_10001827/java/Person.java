





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String name;
    private String gender;
    private String phoneNumber;
    private String title;
    private String address;





    private Hospital hospital;


    public Person(
        String name,        String gender,        String phoneNumber,        String title,        String address    ) {
        this.name = name;
        this.gender = gender;
        this.phoneNumber = phoneNumber;
        this.title = title;
        this.address = address;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }

}