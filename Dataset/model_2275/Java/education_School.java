





import java.util.List;
import java.util.ArrayList;

public class education_School  {

    private String name;
    private String address;
    private String phone;





    private education_Course education_course;




    private List<education_Course> education_courses;


    public education_School(
        String name,        String address,        String phone    ) {
        this.name = name;
        this.address = address;
        this.phone = phone;
        this.education_courses = new ArrayList<>();
    }

    public education_School(
        String name,        String address,        String phone        ArrayList<education_Course> education_courses    ) {
        this.name = name;
        this.address = address;
        this.phone = phone;
        this.education_courses = education_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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

}