





import java.util.List;
import java.util.ArrayList;

public class gedcoml_BekanntePerson extends Person {

    private String middleName;
    private String lastName;
    private String birthDay;
    private String birthName;
    private String firstName;
    private String deathDay;





    private gedcoml_Author gedcoml_author;




    private gedcoml_Person gedcoml_person;




    private List<gedcoml_Married> gedcoml_marrieds;




    private List<gedcoml_Source> gedcoml_sources;




    private List<gedcoml_Person> gedcoml_persons;




    private gedcoml_Person gedcoml_person;




    private List<gedcoml_Note> gedcoml_notes;


    public gedcoml_BekanntePerson(
        String middleName,        String lastName,        String birthDay,        String birthName,        String firstName,        String deathDay    ) {
        super(
        );
        this.middleName = middleName;
        this.lastName = lastName;
        this.birthDay = birthDay;
        this.birthName = birthName;
        this.firstName = firstName;
        this.deathDay = deathDay;
        this.gedcoml_marrieds = new ArrayList<>();
        this.gedcoml_sources = new ArrayList<>();
        this.gedcoml_persons = new ArrayList<>();
        this.gedcoml_notes = new ArrayList<>();
    }

    public gedcoml_BekanntePerson(
        String middleName,        String lastName,        String birthDay,        String birthName,        String firstName,        String deathDay        ArrayList<gedcoml_Married> gedcoml_marrieds,        ArrayList<gedcoml_Source> gedcoml_sources,        ArrayList<gedcoml_Person> gedcoml_persons,        ArrayList<gedcoml_Note> gedcoml_notes    ) {
        this.middleName = middleName;
        this.lastName = lastName;
        this.birthDay = birthDay;
        this.birthName = birthName;
        this.firstName = firstName;
        this.deathDay = deathDay;
        this.gedcoml_marrieds = gedcoml_marrieds;
        this.gedcoml_sources = gedcoml_sources;
        this.gedcoml_persons = gedcoml_persons;
        this.gedcoml_notes = gedcoml_notes;
    }

    public String getMiddlename() {
        return middleName;
    }

    public void setMiddlename(String middleName) {
        this.middleName = middleName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getBirthday() {
        return birthDay;
    }

    public void setBirthday(String birthDay) {
        this.birthDay = birthDay;
    }
    public String getBirthname() {
        return birthName;
    }

    public void setBirthname(String birthName) {
        this.birthName = birthName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getDeathday() {
        return deathDay;
    }

    public void setDeathday(String deathDay) {
        this.deathDay = deathDay;
    }

    public gedcoml_Author getGedcoml_author() {
        return gedcoml_author;
    }

    public void setGedcoml_author(gedcoml_Author gedcoml_author) {
        this.gedcoml_author = gedcoml_author;
    }
    public gedcoml_Person getGedcoml_person() {
        return gedcoml_person;
    }

    public void setGedcoml_person(gedcoml_Person gedcoml_person) {
        this.gedcoml_person = gedcoml_person;
    }
    public List<gedcoml_Married> getGedcoml_marrieds() {
        return gedcoml_marrieds;
    }

    public void addGedcoml_married(Gedcoml_married gedcoml_married) {
        this.gedcoml_marrieds.add(gedcoml_married);
    }
    public List<gedcoml_Source> getGedcoml_sources() {
        return gedcoml_sources;
    }

    public void addGedcoml_source(Gedcoml_source gedcoml_source) {
        this.gedcoml_sources.add(gedcoml_source);
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
    public List<gedcoml_Note> getGedcoml_notes() {
        return gedcoml_notes;
    }

    public void addGedcoml_note(Gedcoml_note gedcoml_note) {
        this.gedcoml_notes.add(gedcoml_note);
    }

}