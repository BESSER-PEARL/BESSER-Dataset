




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class students  {

    private String address;
    private LocalDate birthdate;
    private String gender;
    private String name;
    private String id;



    public students(
        String address,        LocalDate birthdate,        String gender,        String name,        String id    ) {
        this.address = address;
        this.birthdate = birthdate;
        this.gender = gender;
        this.name = name;
        this.id = id;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public LocalDate getBirthdate() {
        return birthdate;
    }

    public void setBirthdate(LocalDate birthdate) {
        this.birthdate = birthdate;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}