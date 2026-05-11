




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_Person extends InformationObject {

    private String title;
    private String firstname;
    private LocalDate dateOfBirth;
    private String lastname;





    private List<data_Person> data_persons;


    public data_Person(
        String title,        String firstname,        LocalDate dateOfBirth,        String lastname    ) {
        super(
        );
        this.title = title;
        this.firstname = firstname;
        this.dateOfBirth = dateOfBirth;
        this.lastname = lastname;
        this.data_persons = new ArrayList<>();
    }

    public data_Person(
        String title,        String firstname,        LocalDate dateOfBirth,        String lastname        ArrayList<data_Person> data_persons    ) {
        this.title = title;
        this.firstname = firstname;
        this.dateOfBirth = dateOfBirth;
        this.lastname = lastname;
        this.data_persons = data_persons;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public List<data_Person> getData_persons() {
        return data_persons;
    }

    public void addData_person(Data_person data_person) {
        this.data_persons.add(data_person);
    }

}