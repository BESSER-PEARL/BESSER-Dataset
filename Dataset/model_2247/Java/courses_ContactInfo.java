





import java.util.List;
import java.util.ArrayList;

public class courses_ContactInfo  {

    private String phone;
    private String department;





    private courses_Person courses_person;




    private List<courses_Person> courses_persons;




    private courses_CourseInstance courses_courseinstance;


    public courses_ContactInfo(
        String phone,        String department    ) {
        this.phone = phone;
        this.department = department;
        this.courses_persons = new ArrayList<>();
    }

    public courses_ContactInfo(
        String phone,        String department        ArrayList<courses_Person> courses_persons    ) {
        this.phone = phone;
        this.department = department;
        this.courses_persons = courses_persons;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public courses_Person getCourses_person() {
        return courses_person;
    }

    public void setCourses_person(courses_Person courses_person) {
        this.courses_person = courses_person;
    }
    public List<courses_Person> getCourses_persons() {
        return courses_persons;
    }

    public void addCourses_person(Courses_person courses_person) {
        this.courses_persons.add(courses_person);
    }
    public courses_CourseInstance getCourses_courseinstance() {
        return courses_courseinstance;
    }

    public void setCourses_courseinstance(courses_CourseInstance courses_courseinstance) {
        this.courses_courseinstance = courses_courseinstance;
    }

}