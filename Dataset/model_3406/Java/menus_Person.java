




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class menus_Person  {

    private boolean pregnant;
    private String firstname;
    private LocalDate dateOfBirth;
    private String sex;
    private String lastname;





    private menus_Person menus_person;


    public menus_Person(
        boolean pregnant,        String firstname,        LocalDate dateOfBirth,        String sex,        String lastname    ) {
        this.pregnant = pregnant;
        this.firstname = firstname;
        this.dateOfBirth = dateOfBirth;
        this.sex = sex;
        this.lastname = lastname;
    }


    public boolean getPregnant() {
        return pregnant;
    }

    public void setPregnant(boolean pregnant) {
        this.pregnant = pregnant;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public menus_Person getMenus_person() {
        return menus_person;
    }

    public void setMenus_person(menus_Person menus_person) {
        this.menus_person = menus_person;
    }

}