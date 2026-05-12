




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String address;
    private String Gender;
    private String Title;
    private LocalDate birthDate;
    private int phone;
    private String Name;



    public Person(
        String address,        String Gender,        String Title,        LocalDate birthDate,        int phone,        String Name    ) {
        this.address = address;
        this.Gender = Gender;
        this.Title = Title;
        this.birthDate = birthDate;
        this.phone = phone;
        this.Name = Name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public LocalDate getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}