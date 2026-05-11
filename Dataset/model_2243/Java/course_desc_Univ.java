





import java.util.List;
import java.util.ArrayList;

public class course_desc_Univ  {






    private List<course_desc_Person> course_desc_persons;




    private List<course_desc_Student> course_desc_students;


    public course_desc_Univ(
    ) {
        this.course_desc_persons = new ArrayList<>();
        this.course_desc_students = new ArrayList<>();
    }

    public course_desc_Univ(
        ArrayList<course_desc_Person> course_desc_persons,        ArrayList<course_desc_Student> course_desc_students    ) {
        this.course_desc_persons = course_desc_persons;
        this.course_desc_students = course_desc_students;
    }


    public List<course_desc_Person> getCourse_desc_persons() {
        return course_desc_persons;
    }

    public void addCourse_desc_person(Course_desc_person course_desc_person) {
        this.course_desc_persons.add(course_desc_person);
    }
    public List<course_desc_Student> getCourse_desc_students() {
        return course_desc_students;
    }

    public void addCourse_desc_student(Course_desc_student course_desc_student) {
        this.course_desc_students.add(course_desc_student);
    }

}