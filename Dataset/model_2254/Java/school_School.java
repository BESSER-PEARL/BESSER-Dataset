





import java.util.List;
import java.util.ArrayList;

public class school_School  {

    private String name;
    private String address;
    private int currentYear;
    private int numberOfTeachers;





    private List<school_Course> school_courses;




    private school_Course school_course;


    public school_School(
        String name,        String address,        int currentYear,        int numberOfTeachers    ) {
        this.name = name;
        this.address = address;
        this.currentYear = currentYear;
        this.numberOfTeachers = numberOfTeachers;
        this.school_courses = new ArrayList<>();
    }

    public school_School(
        String name,        String address,        int currentYear,        int numberOfTeachers        ArrayList<school_Course> school_courses    ) {
        this.name = name;
        this.address = address;
        this.currentYear = currentYear;
        this.numberOfTeachers = numberOfTeachers;
        this.school_courses = school_courses;
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
    public int getCurrentyear() {
        return currentYear;
    }

    public void setCurrentyear(int currentYear) {
        this.currentYear = currentYear;
    }
    public int getNumberofteachers() {
        return numberOfTeachers;
    }

    public void setNumberofteachers(int numberOfTeachers) {
        this.numberOfTeachers = numberOfTeachers;
    }

    public List<school_Course> getSchool_courses() {
        return school_courses;
    }

    public void addSchool_course(School_course school_course) {
        this.school_courses.add(school_course);
    }
    public school_Course getSchool_course() {
        return school_course;
    }

    public void setSchool_course(school_Course school_course) {
        this.school_course = school_course;
    }

}