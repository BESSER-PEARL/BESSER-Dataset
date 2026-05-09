




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class library_Author  {

    private String surname;
    private String name;
    private LocalDate birthdate;



    public library_Author(
        String surname,        String name,        LocalDate birthdate    ) {
        this.surname = surname;
        this.name = name;
        this.birthdate = birthdate;
    }


    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getBirthdate() {
        return birthdate;
    }

    public void setBirthdate(LocalDate birthdate) {
        this.birthdate = birthdate;
    }


}