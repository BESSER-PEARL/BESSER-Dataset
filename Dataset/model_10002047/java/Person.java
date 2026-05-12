




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String address;
    private int phone;
    private LocalDate birthDate;
    private String Gender;
    private String Title;
    private String Name;



    public Person(
        String address,        int phone,        LocalDate birthDate,        String Gender,        String Title,        String Name    ) {
        this.address = address;
        this.phone = phone;
        this.birthDate = birthDate;
        this.Gender = Gender;
        this.Title = Title;
        this.Name = Name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public LocalDate getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(LocalDate birthDate) {
        this.birthDate = birthDate;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}