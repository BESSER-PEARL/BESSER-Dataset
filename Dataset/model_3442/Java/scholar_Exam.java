





import java.util.List;
import java.util.ArrayList;

public class scholar_Exam extends Named {

    private float score;





    private scholar_Student scholar_student;


    public scholar_Exam(
        float score    ) {
        super(
        );
        this.score = score;
    }


    public float getScore() {
        return score;
    }

    public void setScore(float score) {
        this.score = score;
    }

    public scholar_Student getScholar_student() {
        return scholar_student;
    }

    public void setScholar_student(scholar_Student scholar_student) {
        this.scholar_student = scholar_student;
    }

}