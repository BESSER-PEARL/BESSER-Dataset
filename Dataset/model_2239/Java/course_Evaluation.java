





import java.util.List;
import java.util.ArrayList;

public class course_Evaluation  {

    private int assigments;
    private int project;
    private int exam;



    public course_Evaluation(
        int assigments,        int project,        int exam    ) {
        this.assigments = assigments;
        this.project = project;
        this.exam = exam;
    }


    public int getAssigments() {
        return assigments;
    }

    public void setAssigments(int assigments) {
        this.assigments = assigments;
    }
    public int getProject() {
        return project;
    }

    public void setProject(int project) {
        this.project = project;
    }
    public int getExam() {
        return exam;
    }

    public void setExam(int exam) {
        this.exam = exam;
    }


}