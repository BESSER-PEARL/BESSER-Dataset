




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class menus_Person  {

    private String lastname;
    private boolean pregnant;
    private LocalDate dateOfBirth;
    private String sex;
    private String firstname;





    private menus_Person menus_person;


    public menus_Person(
        String lastname,        boolean pregnant,        LocalDate dateOfBirth,        String sex,        String firstname    ) {
        this.lastname = lastname;
        this.pregnant = pregnant;
        this.dateOfBirth = dateOfBirth;
        this.sex = sex;
        this.firstname = firstname;
    }


    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public boolean getPregnant() {
        return pregnant;
    }

    public void setPregnant(boolean pregnant) {
        this.pregnant = pregnant;
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
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public menus_Person getMenus_person() {
        return menus_person;
    }

    public void setMenus_person(menus_Person menus_person) {
        this.menus_person = menus_person;
    }

}