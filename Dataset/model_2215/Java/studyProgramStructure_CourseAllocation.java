





import java.util.List;
import java.util.ArrayList;

public class studyProgramStructure_CourseAllocation  {

    private String grade;





    private studyProgramStructure_StudyPlan studyprogramstructure_studyplan;




    private studyProgramStructure_Course studyprogramstructure_course;


    public studyProgramStructure_CourseAllocation(
        String grade    ) {
        this.grade = grade;
    }


    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }

    public studyProgramStructure_StudyPlan getStudyprogramstructure_studyplan() {
        return studyprogramstructure_studyplan;
    }

    public void setStudyprogramstructure_studyplan(studyProgramStructure_StudyPlan studyprogramstructure_studyplan) {
        this.studyprogramstructure_studyplan = studyprogramstructure_studyplan;
    }
    public studyProgramStructure_Course getStudyprogramstructure_course() {
        return studyprogramstructure_course;
    }

    public void setStudyprogramstructure_course(studyProgramStructure_Course studyprogramstructure_course) {
        this.studyprogramstructure_course = studyprogramstructure_course;
    }

}