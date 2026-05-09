





import java.util.List;
import java.util.ArrayList;

public class family_Person extends EModelElement {

    private String birthMonth;
    private String firstName;
    private int birthYear;
    private String birthCity;
    private int birthDay;
    private String lastName;





    private family_Person family_person;


    public family_Person(
        String birthMonth,        String firstName,        int birthYear,        String birthCity,        int birthDay,        String lastName    ) {
        super(
        );
        this.birthMonth = birthMonth;
        this.firstName = firstName;
        this.birthYear = birthYear;
        this.birthCity = birthCity;
        this.birthDay = birthDay;
        this.lastName = lastName;
    }


    public String getBirthmonth() {
        return birthMonth;
    }

    public void setBirthmonth(String birthMonth) {
        this.birthMonth = birthMonth;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public int getBirthyear() {
        return birthYear;
    }

    public void setBirthyear(int birthYear) {
        this.birthYear = birthYear;
    }
    public String getBirthcity() {
        return birthCity;
    }

    public void setBirthcity(String birthCity) {
        this.birthCity = birthCity;
    }
    public int getBirthday() {
        return birthDay;
    }

    public void setBirthday(int birthDay) {
        this.birthDay = birthDay;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public family_Person getFamily_person() {
        return family_person;
    }

    public void setFamily_person(family_Person family_person) {
        this.family_person = family_person;
    }

}