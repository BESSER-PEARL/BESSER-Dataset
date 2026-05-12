





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private None teachers__;
    private None students__;
    private None course;
    private None hod;



    public Department(
        None teachers__,        None students__,        None course,        None hod    ) {
        this.teachers__ = teachers__;
        this.students__ = students__;
        this.course = course;
        this.hod = hod;
    }


    public None getTeachers__() {
        return teachers__;
    }

    public void setTeachers__(None teachers__) {
        this.teachers__ = teachers__;
    }
    public None getStudents__() {
        return students__;
    }

    public void setStudents__(None students__) {
        this.students__ = students__;
    }
    public None getCourse() {
        return course;
    }

    public void setCourse(None course) {
        this.course = course;
    }
    public None getHod() {
        return hod;
    }

    public void setHod(None hod) {
        this.hod = hod;
    }


}