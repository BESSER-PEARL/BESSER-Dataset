





import java.util.List;
import java.util.ArrayList;

public class lobj_Person  {

    private String honorific;
    private String firstname;
    private String surname;
    private String contrib;
    private String personblurb;
    private String id;





    private List<lobj_Affiliation> lobj_affiliations;




    private lobj_Author lobj_author;


    public lobj_Person(
        String honorific,        String firstname,        String surname,        String contrib,        String personblurb,        String id    ) {
        this.honorific = honorific;
        this.firstname = firstname;
        this.surname = surname;
        this.contrib = contrib;
        this.personblurb = personblurb;
        this.id = id;
        this.lobj_affiliations = new ArrayList<>();
    }

    public lobj_Person(
        String honorific,        String firstname,        String surname,        String contrib,        String personblurb,        String id        ArrayList<lobj_Affiliation> lobj_affiliations    ) {
        this.honorific = honorific;
        this.firstname = firstname;
        this.surname = surname;
        this.contrib = contrib;
        this.personblurb = personblurb;
        this.id = id;
        this.lobj_affiliations = lobj_affiliations;
    }

    public String getHonorific() {
        return honorific;
    }

    public void setHonorific(String honorific) {
        this.honorific = honorific;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getContrib() {
        return contrib;
    }

    public void setContrib(String contrib) {
        this.contrib = contrib;
    }
    public String getPersonblurb() {
        return personblurb;
    }

    public void setPersonblurb(String personblurb) {
        this.personblurb = personblurb;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<lobj_Affiliation> getLobj_affiliations() {
        return lobj_affiliations;
    }

    public void addLobj_affiliation(Lobj_affiliation lobj_affiliation) {
        this.lobj_affiliations.add(lobj_affiliation);
    }
    public lobj_Author getLobj_author() {
        return lobj_author;
    }

    public void setLobj_author(lobj_Author lobj_author) {
        this.lobj_author = lobj_author;
    }

}