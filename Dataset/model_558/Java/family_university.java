





import java.util.List;
import java.util.ArrayList;

public class family_university  {

    private String name;





    private family_person family_person;




    private List<family_course> family_courses;


    public family_university(
        String name    ) {
        this.name = name;
        this.family_courses = new ArrayList<>();
    }

    public family_university(
        String name        ArrayList<family_course> family_courses    ) {
        this.name = name;
        this.family_courses = family_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public family_person getFamily_person() {
        return family_person;
    }

    public void setFamily_person(family_person family_person) {
        this.family_person = family_person;
    }
    public List<family_course> getFamily_courses() {
        return family_courses;
    }

    public void addFamily_course(Family_course family_course) {
        this.family_courses.add(family_course);
    }

}