





import java.util.List;
import java.util.ArrayList;

public class family_Person extends NamedElement {

    private String gender;
    private String surname;
    private int age;





    private family_Members family_members;


    public family_Person(
        String gender,        String surname,        int age    ) {
        super(
        );
        this.gender = gender;
        this.surname = surname;
        this.age = age;
    }


    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public family_Members getFamily_members() {
        return family_members;
    }

    public void setFamily_members(family_Members family_members) {
        this.family_members = family_members;
    }

}