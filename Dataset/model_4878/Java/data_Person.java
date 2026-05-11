




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_Person extends InformationObject {

    private String firstname;
    private String lastname;
    private LocalDate dateOfBirth;
    private String title;





    private List<data_Content> data_contents;




    private List<data_Person> data_persons;




    private data_Content data_content;




    private List<data_Organisation> data_organisations;




    private data_Ranking data_ranking;




    private data_Organisation data_organisation;




    private data_Organisation data_organisation;




    private List<data_Content> data_contents;




    private List<data_Organisation> data_organisations;




    private data_Content data_content;




    private List<data_Ranking> data_rankings;


    public data_Person(
        String firstname,        String lastname,        LocalDate dateOfBirth,        String title    ) {
        super(
        );
        this.firstname = firstname;
        this.lastname = lastname;
        this.dateOfBirth = dateOfBirth;
        this.title = title;
        this.data_contents = new ArrayList<>();
        this.data_persons = new ArrayList<>();
        this.data_organisations = new ArrayList<>();
        this.data_contents = new ArrayList<>();
        this.data_organisations = new ArrayList<>();
        this.data_rankings = new ArrayList<>();
    }

    public data_Person(
        String firstname,        String lastname,        LocalDate dateOfBirth,        String title        ArrayList<data_Content> data_contents,        ArrayList<data_Person> data_persons,        ArrayList<data_Organisation> data_organisations,        ArrayList<data_Content> data_contents,        ArrayList<data_Organisation> data_organisations,        ArrayList<data_Ranking> data_rankings    ) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.dateOfBirth = dateOfBirth;
        this.title = title;
        this.data_contents = data_contents;
        this.data_persons = data_persons;
        this.data_organisations = data_organisations;
        this.data_contents = data_contents;
        this.data_organisations = data_organisations;
        this.data_rankings = data_rankings;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<data_Content> getData_contents() {
        return data_contents;
    }

    public void addData_content(Data_content data_content) {
        this.data_contents.add(data_content);
    }
    public List<data_Person> getData_persons() {
        return data_persons;
    }

    public void addData_person(Data_person data_person) {
        this.data_persons.add(data_person);
    }
    public data_Content getData_content() {
        return data_content;
    }

    public void setData_content(data_Content data_content) {
        this.data_content = data_content;
    }
    public List<data_Organisation> getData_organisations() {
        return data_organisations;
    }

    public void addData_organisation(Data_organisation data_organisation) {
        this.data_organisations.add(data_organisation);
    }
    public data_Ranking getData_ranking() {
        return data_ranking;
    }

    public void setData_ranking(data_Ranking data_ranking) {
        this.data_ranking = data_ranking;
    }
    public data_Organisation getData_organisation() {
        return data_organisation;
    }

    public void setData_organisation(data_Organisation data_organisation) {
        this.data_organisation = data_organisation;
    }
    public data_Organisation getData_organisation() {
        return data_organisation;
    }

    public void setData_organisation(data_Organisation data_organisation) {
        this.data_organisation = data_organisation;
    }
    public List<data_Content> getData_contents() {
        return data_contents;
    }

    public void addData_content(Data_content data_content) {
        this.data_contents.add(data_content);
    }
    public List<data_Organisation> getData_organisations() {
        return data_organisations;
    }

    public void addData_organisation(Data_organisation data_organisation) {
        this.data_organisations.add(data_organisation);
    }
    public data_Content getData_content() {
        return data_content;
    }

    public void setData_content(data_Content data_content) {
        this.data_content = data_content;
    }
    public List<data_Ranking> getData_rankings() {
        return data_rankings;
    }

    public void addData_ranking(Data_ranking data_ranking) {
        this.data_rankings.add(data_ranking);
    }

}