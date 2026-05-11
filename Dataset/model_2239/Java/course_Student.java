





import java.util.List;
import java.util.ArrayList;

public class course_Student extends Person {






    private course_StudyProgram course_studyprogram;




    private course_StudyProgram course_studyprogram;




    private course_Evaluation course_evaluation;




    private List<course_Evaluation> course_evaluations;


    public course_Student(
    ) {
        super(
        );
        this.course_evaluations = new ArrayList<>();
    }

    public course_Student(
        ArrayList<course_Evaluation> course_evaluations    ) {
        this.course_evaluations = course_evaluations;
    }


    public course_StudyProgram getCourse_studyprogram() {
        return course_studyprogram;
    }

    public void setCourse_studyprogram(course_StudyProgram course_studyprogram) {
        this.course_studyprogram = course_studyprogram;
    }
    public course_StudyProgram getCourse_studyprogram() {
        return course_studyprogram;
    }

    public void setCourse_studyprogram(course_StudyProgram course_studyprogram) {
        this.course_studyprogram = course_studyprogram;
    }
    public course_Evaluation getCourse_evaluation() {
        return course_evaluation;
    }

    public void setCourse_evaluation(course_Evaluation course_evaluation) {
        this.course_evaluation = course_evaluation;
    }
    public List<course_Evaluation> getCourse_evaluations() {
        return course_evaluations;
    }

    public void addCourse_evaluation(Course_evaluation course_evaluation) {
        this.course_evaluations.add(course_evaluation);
    }

}