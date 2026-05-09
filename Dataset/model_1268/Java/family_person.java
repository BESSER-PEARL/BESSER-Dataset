





import java.util.List;
import java.util.ArrayList;

public class family_person  {

    private String name;
    private String cpr;
    private String age;





    private family_person family_person;




    private family_family family_family;




    private List<family_person> family_persons;




    private family_studyprogramme family_studyprogramme;




    private List<family_person> family_persons;


    public family_person(
        String name,        String cpr,        String age    ) {
        this.name = name;
        this.cpr = cpr;
        this.age = age;
        this.family_persons = new ArrayList<>();
        this.family_persons = new ArrayList<>();
    }

    public family_person(
        String name,        String cpr,        String age        ArrayList<family_person> family_persons,        ArrayList<family_person> family_persons    ) {
        this.name = name;
        this.cpr = cpr;
        this.age = age;
        this.family_persons = family_persons;
        this.family_persons = family_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCpr() {
        return cpr;
    }

    public void setCpr(String cpr) {
        this.cpr = cpr;
    }
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public family_person getFamily_person() {
        return family_person;
    }

    public void setFamily_person(family_person family_person) {
        this.family_person = family_person;
    }
    public family_family getFamily_family() {
        return family_family;
    }

    public void setFamily_family(family_family family_family) {
        this.family_family = family_family;
    }
    public List<family_person> getFamily_persons() {
        return family_persons;
    }

    public void addFamily_person(Family_person family_person) {
        this.family_persons.add(family_person);
    }
    public family_studyprogramme getFamily_studyprogramme() {
        return family_studyprogramme;
    }

    public void setFamily_studyprogramme(family_studyprogramme family_studyprogramme) {
        this.family_studyprogramme = family_studyprogramme;
    }
    public List<family_person> getFamily_persons() {
        return family_persons;
    }

    public void addFamily_person(Family_person family_person) {
        this.family_persons.add(family_person);
    }

}