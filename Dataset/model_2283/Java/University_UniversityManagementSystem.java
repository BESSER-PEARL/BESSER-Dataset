





import java.util.List;
import java.util.ArrayList;

public class University_UniversityManagementSystem  {






    private List<University_Person> university_persons;




    private List<University_Course> university_courses;


    public University_UniversityManagementSystem(
    ) {
        this.university_persons = new ArrayList<>();
        this.university_courses = new ArrayList<>();
    }

    public University_UniversityManagementSystem(
        ArrayList<University_Person> university_persons,        ArrayList<University_Course> university_courses    ) {
        this.university_persons = university_persons;
        this.university_courses = university_courses;
    }


    public List<University_Person> getUniversity_persons() {
        return university_persons;
    }

    public void addUniversity_person(University_person university_person) {
        this.university_persons.add(university_person);
    }
    public List<University_Course> getUniversity_courses() {
        return university_courses;
    }

    public void addUniversity_course(University_course university_course) {
        this.university_courses.add(university_course);
    }

}