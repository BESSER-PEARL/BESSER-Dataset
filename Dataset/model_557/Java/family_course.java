





import java.util.List;
import java.util.ArrayList;

public class family_course  {

    private String name;





    private family_university family_university;




    private List<family_person> family_persons;


    public family_course(
        String name    ) {
        this.name = name;
        this.family_persons = new ArrayList<>();
    }

    public family_course(
        String name        ArrayList<family_person> family_persons    ) {
        this.name = name;
        this.family_persons = family_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public family_university getFamily_university() {
        return family_university;
    }

    public void setFamily_university(family_university family_university) {
        this.family_university = family_university;
    }
    public List<family_person> getFamily_persons() {
        return family_persons;
    }

    public void addFamily_person(Family_person family_person) {
        this.family_persons.add(family_person);
    }

}