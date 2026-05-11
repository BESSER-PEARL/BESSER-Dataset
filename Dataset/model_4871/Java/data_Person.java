




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_Person extends InformationObject {

    private String lastname;
    private String title;
    private String firstname;
    private LocalDate dateOfBirth;





    private data_Organisation data_organisation;




    private List<data_Content> data_contents;




    private data_Ranking data_ranking;




    private List<data_Organisation> data_organisations;




    private List<data_Content> data_contents;




    private List<data_Ranking> data_rankings;




    private List<data_Person> data_persons;




    private List<data_Organisation> data_organisations;




    private data_Content data_content;




    private data_Content data_content;




    private data_Organisation data_organisation;


    public data_Person(
        String lastname,        String title,        String firstname,        LocalDate dateOfBirth    ) {
        super(
        );
        this.lastname = lastname;
        this.title = title;
        this.firstname = firstname;
        this.dateOfBirth = dateOfBirth;
        this.data_contents = new ArrayList<>();
        this.data_organisations = new ArrayList<>();
        this.data_contents = new ArrayList<>();
        this.data_rankings = new ArrayList<>();
        this.data_persons = new ArrayList<>();
        this.data_organisations = new ArrayList<>();
    }

    public data_Person(
        String lastname,        String title,        String firstname,        LocalDate dateOfBirth        ArrayList<data_Content> data_contents,        ArrayList<data_Organisation> data_organisations,        ArrayList<data_Content> data_contents,        ArrayList<data_Ranking> data_rankings,        ArrayList<data_Person> data_persons,        ArrayList<data_Organisation> data_organisations    ) {
        this.lastname = lastname;
        this.title = title;
        this.firstname = firstname;
        this.dateOfBirth = dateOfBirth;
        this.data_contents = data_contents;
        this.data_organisations = data_organisations;
        this.data_contents = data_contents;
        this.data_rankings = data_rankings;
        this.data_persons = data_persons;
        this.data_organisations = data_organisations;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
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
    public data_Ranking getData_ranking() {
        return data_ranking;
    }

    public void setData_ranking(data_Ranking data_ranking) {
        this.data_ranking = data_ranking;
    }
    public List<data_Organisation> getData_organisations() {
        return data_organisations;
    }

    public void addData_organisation(Data_organisation data_organisation) {
        this.data_organisations.add(data_organisation);
    }
    public List<data_Content> getData_contents() {
        return data_contents;
    }

    public void addData_content(Data_content data_content) {
        this.data_contents.add(data_content);
    }
    public List<data_Ranking> getData_rankings() {
        return data_rankings;
    }

    public void addData_ranking(Data_ranking data_ranking) {
        this.data_rankings.add(data_ranking);
    }
    public List<data_Person> getData_persons() {
        return data_persons;
    }

    public void addData_person(Data_person data_person) {
        this.data_persons.add(data_person);
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
    public data_Content getData_content() {
        return data_content;
    }

    public void setData_content(data_Content data_content) {
        this.data_content = data_content;
    }
    public data_Organisation getData_organisation() {
        return data_organisation;
    }

    public void setData_organisation(data_Organisation data_organisation) {
        this.data_organisation = data_organisation;
    }

}