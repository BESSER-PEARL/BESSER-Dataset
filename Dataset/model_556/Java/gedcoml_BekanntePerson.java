





import java.util.List;
import java.util.ArrayList;

public class gedcoml_BekanntePerson extends Person {

    private String deathDay;
    private String lastName;
    private String middleName;
    private String birthDay;
    private String firstName;
    private String birthName;





    private List<gedcoml_Person> gedcoml_persons;




    private gedcoml_Person gedcoml_person;




    private gedcoml_Person gedcoml_person;




    private gedcoml_Author gedcoml_author;


    public gedcoml_BekanntePerson(
        String deathDay,        String lastName,        String middleName,        String birthDay,        String firstName,        String birthName    ) {
        super(
        );
        this.deathDay = deathDay;
        this.lastName = lastName;
        this.middleName = middleName;
        this.birthDay = birthDay;
        this.firstName = firstName;
        this.birthName = birthName;
        this.gedcoml_persons = new ArrayList<>();
    }

    public gedcoml_BekanntePerson(
        String deathDay,        String lastName,        String middleName,        String birthDay,        String firstName,        String birthName        ArrayList<gedcoml_Person> gedcoml_persons    ) {
        this.deathDay = deathDay;
        this.lastName = lastName;
        this.middleName = middleName;
        this.birthDay = birthDay;
        this.firstName = firstName;
        this.birthName = birthName;
        this.gedcoml_persons = gedcoml_persons;
    }

    public String getDeathday() {
        return deathDay;
    }

    public void setDeathday(String deathDay) {
        this.deathDay = deathDay;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getMiddlename() {
        return middleName;
    }

    public void setMiddlename(String middleName) {
        this.middleName = middleName;
    }
    public String getBirthday() {
        return birthDay;
    }

    public void setBirthday(String birthDay) {
        this.birthDay = birthDay;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getBirthname() {
        return birthName;
    }

    public void setBirthname(String birthName) {
        this.birthName = birthName;
    }

    public List<gedcoml_Person> getGedcoml_persons() {
        return gedcoml_persons;
    }

    public void addGedcoml_person(Gedcoml_person gedcoml_person) {
        this.gedcoml_persons.add(gedcoml_person);
    }
    public gedcoml_Person getGedcoml_person() {
        return gedcoml_person;
    }

    public void setGedcoml_person(gedcoml_Person gedcoml_person) {
        this.gedcoml_person = gedcoml_person;
    }
    public gedcoml_Person getGedcoml_person() {
        return gedcoml_person;
    }

    public void setGedcoml_person(gedcoml_Person gedcoml_person) {
        this.gedcoml_person = gedcoml_person;
    }
    public gedcoml_Author getGedcoml_author() {
        return gedcoml_author;
    }

    public void setGedcoml_author(gedcoml_Author gedcoml_author) {
        this.gedcoml_author = gedcoml_author;
    }

}