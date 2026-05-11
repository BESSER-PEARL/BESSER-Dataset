





import java.util.List;
import java.util.ArrayList;

public class school_SchoolStatistics  {

    private int teachersNumber;
    private int studentsNumber;
    private String studentsWithNoTeacher;





    private school_School school_school;


    public school_SchoolStatistics(
        int teachersNumber,        int studentsNumber,        String studentsWithNoTeacher    ) {
        this.teachersNumber = teachersNumber;
        this.studentsNumber = studentsNumber;
        this.studentsWithNoTeacher = studentsWithNoTeacher;
    }


    public int getTeachersnumber() {
        return teachersNumber;
    }

    public void setTeachersnumber(int teachersNumber) {
        this.teachersNumber = teachersNumber;
    }
    public int getStudentsnumber() {
        return studentsNumber;
    }

    public void setStudentsnumber(int studentsNumber) {
        this.studentsNumber = studentsNumber;
    }
    public String getStudentswithnoteacher() {
        return studentsWithNoTeacher;
    }

    public void setStudentswithnoteacher(String studentsWithNoTeacher) {
        this.studentsWithNoTeacher = studentsWithNoTeacher;
    }

    public school_School getSchool_school() {
        return school_school;
    }

    public void setSchool_school(school_School school_school) {
        this.school_school = school_school;
    }

}