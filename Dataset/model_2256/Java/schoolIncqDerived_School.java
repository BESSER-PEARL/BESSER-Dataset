





import java.util.List;
import java.util.ArrayList;

public class schoolIncqDerived_School  {

    private int currentYear;
    private String address;
    private String name;
    private int numberOfTeachers;





    private List<schoolIncqDerived_Course> schoolincqderived_courses;




    private schoolIncqDerived_Course schoolincqderived_course;


    public schoolIncqDerived_School(
        int currentYear,        String address,        String name,        int numberOfTeachers    ) {
        this.currentYear = currentYear;
        this.address = address;
        this.name = name;
        this.numberOfTeachers = numberOfTeachers;
        this.schoolincqderived_courses = new ArrayList<>();
    }

    public schoolIncqDerived_School(
        int currentYear,        String address,        String name,        int numberOfTeachers        ArrayList<schoolIncqDerived_Course> schoolincqderived_courses    ) {
        this.currentYear = currentYear;
        this.address = address;
        this.name = name;
        this.numberOfTeachers = numberOfTeachers;
        this.schoolincqderived_courses = schoolincqderived_courses;
    }

    public int getCurrentyear() {
        return currentYear;
    }

    public void setCurrentyear(int currentYear) {
        this.currentYear = currentYear;
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
    public int getNumberofteachers() {
        return numberOfTeachers;
    }

    public void setNumberofteachers(int numberOfTeachers) {
        this.numberOfTeachers = numberOfTeachers;
    }

    public List<schoolIncqDerived_Course> getSchoolincqderived_courses() {
        return schoolincqderived_courses;
    }

    public void addSchoolincqderived_course(Schoolincqderived_course schoolincqderived_course) {
        this.schoolincqderived_courses.add(schoolincqderived_course);
    }
    public schoolIncqDerived_Course getSchoolincqderived_course() {
        return schoolincqderived_course;
    }

    public void setSchoolincqderived_course(schoolIncqDerived_Course schoolincqderived_course) {
        this.schoolincqderived_course = schoolincqderived_course;
    }

}