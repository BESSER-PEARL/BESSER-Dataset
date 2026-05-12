




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Course  {

    private LocalDate CourseStartDate;
    private None subjects__;
    private String courseName;
    private String courseDuration;
    private LocalDate CourseEndDate;





    private Department department;


    public Course(
        LocalDate CourseStartDate,        None subjects__,        String courseName,        String courseDuration,        LocalDate CourseEndDate    ) {
        this.CourseStartDate = CourseStartDate;
        this.subjects__ = subjects__;
        this.courseName = courseName;
        this.courseDuration = courseDuration;
        this.CourseEndDate = CourseEndDate;
    }


    public LocalDate getCoursestartdate() {
        return CourseStartDate;
    }

    public void setCoursestartdate(LocalDate CourseStartDate) {
        this.CourseStartDate = CourseStartDate;
    }
    public None getSubjects__() {
        return subjects__;
    }

    public void setSubjects__(None subjects__) {
        this.subjects__ = subjects__;
    }
    public String getCoursename() {
        return courseName;
    }

    public void setCoursename(String courseName) {
        this.courseName = courseName;
    }
    public String getCourseduration() {
        return courseDuration;
    }

    public void setCourseduration(String courseDuration) {
        this.courseDuration = courseDuration;
    }
    public LocalDate getCourseenddate() {
        return CourseEndDate;
    }

    public void setCourseenddate(LocalDate CourseEndDate) {
        this.CourseEndDate = CourseEndDate;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}