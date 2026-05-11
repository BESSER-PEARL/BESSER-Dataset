





import java.util.List;
import java.util.ArrayList;

public class education_School  {

    private String address;
    private String name;
    private String phone;





    private education_Course education_course;




    private List<education_Course> education_courses;




    private education_Student education_student;




    private List<education_Student> education_students;


    public education_School(
        String address,        String name,        String phone    ) {
        this.address = address;
        this.name = name;
        this.phone = phone;
        this.education_courses = new ArrayList<>();
        this.education_students = new ArrayList<>();
    }

    public education_School(
        String address,        String name,        String phone        ArrayList<education_Course> education_courses,        ArrayList<education_Student> education_students    ) {
        this.address = address;
        this.name = name;
        this.phone = phone;
        this.education_courses = education_courses;
        this.education_students = education_students;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public education_Course getEducation_course() {
        return education_course;
    }

    public void setEducation_course(education_Course education_course) {
        this.education_course = education_course;
    }
    public List<education_Course> getEducation_courses() {
        return education_courses;
    }

    public void addEducation_course(Education_course education_course) {
        this.education_courses.add(education_course);
    }
    public education_Student getEducation_student() {
        return education_student;
    }

    public void setEducation_student(education_Student education_student) {
        this.education_student = education_student;
    }
    public List<education_Student> getEducation_students() {
        return education_students;
    }

    public void addEducation_student(Education_student education_student) {
        this.education_students.add(education_student);
    }

}