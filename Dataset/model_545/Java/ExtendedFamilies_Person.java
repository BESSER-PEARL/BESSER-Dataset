





import java.util.List;
import java.util.ArrayList;

public class ExtendedFamilies_Person  {

    private String firstName;





    private ExtendedFamilies_Family extendedfamilies_family;




    private List<ExtendedFamilies_Person> extendedfamilies_persons;




    private List<ExtendedFamilies_Person> extendedfamilies_persons;




    private ExtendedFamilies_Family extendedfamilies_family;


    public ExtendedFamilies_Person(
        String firstName    ) {
        this.firstName = firstName;
        this.extendedfamilies_persons = new ArrayList<>();
        this.extendedfamilies_persons = new ArrayList<>();
    }

    public ExtendedFamilies_Person(
        String firstName        ArrayList<ExtendedFamilies_Person> extendedfamilies_persons,        ArrayList<ExtendedFamilies_Person> extendedfamilies_persons    ) {
        this.firstName = firstName;
        this.extendedfamilies_persons = extendedfamilies_persons;
        this.extendedfamilies_persons = extendedfamilies_persons;
    }

    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public ExtendedFamilies_Family getExtendedfamilies_family() {
        return extendedfamilies_family;
    }

    public void setExtendedfamilies_family(ExtendedFamilies_Family extendedfamilies_family) {
        this.extendedfamilies_family = extendedfamilies_family;
    }
    public List<ExtendedFamilies_Person> getExtendedfamilies_persons() {
        return extendedfamilies_persons;
    }

    public void addExtendedfamilies_person(Extendedfamilies_person extendedfamilies_person) {
        this.extendedfamilies_persons.add(extendedfamilies_person);
    }
    public List<ExtendedFamilies_Person> getExtendedfamilies_persons() {
        return extendedfamilies_persons;
    }

    public void addExtendedfamilies_person(Extendedfamilies_person extendedfamilies_person) {
        this.extendedfamilies_persons.add(extendedfamilies_person);
    }
    public ExtendedFamilies_Family getExtendedfamilies_family() {
        return extendedfamilies_family;
    }

    public void setExtendedfamilies_family(ExtendedFamilies_Family extendedfamilies_family) {
        this.extendedfamilies_family = extendedfamilies_family;
    }

}