





import java.util.List;
import java.util.ArrayList;

public class Subject  {

    private String subjectID;
    private String subjectTest;
    private String name;
    private String subjectType;
    private String subjectCategory;





    private Course course;


    public Subject(
        String subjectID,        String subjectTest,        String name,        String subjectType,        String subjectCategory    ) {
        this.subjectID = subjectID;
        this.subjectTest = subjectTest;
        this.name = name;
        this.subjectType = subjectType;
        this.subjectCategory = subjectCategory;
    }


    public String getSubjectid() {
        return subjectID;
    }

    public void setSubjectid(String subjectID) {
        this.subjectID = subjectID;
    }
    public String getSubjecttest() {
        return subjectTest;
    }

    public void setSubjecttest(String subjectTest) {
        this.subjectTest = subjectTest;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSubjecttype() {
        return subjectType;
    }

    public void setSubjecttype(String subjectType) {
        this.subjectType = subjectType;
    }
    public String getSubjectcategory() {
        return subjectCategory;
    }

    public void setSubjectcategory(String subjectCategory) {
        this.subjectCategory = subjectCategory;
    }

    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
        this.course = course;
    }

}