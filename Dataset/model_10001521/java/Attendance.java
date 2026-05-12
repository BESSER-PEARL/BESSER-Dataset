





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private None student;
    private None course;





    private AcademicRecords academicrecords;


    public Attendance(
        None student,        None course    ) {
        this.student = student;
        this.course = course;
    }


    public None getStudent() {
        return student;
    }

    public void setStudent(None student) {
        this.student = student;
    }
    public None getCourse() {
        return course;
    }

    public void setCourse(None course) {
        this.course = course;
    }

    public AcademicRecords getAcademicrecords() {
        return academicrecords;
    }

    public void setAcademicrecords(AcademicRecords academicrecords) {
        this.academicrecords = academicrecords;
    }

}