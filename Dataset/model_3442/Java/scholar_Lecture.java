





import java.util.List;
import java.util.ArrayList;

public class scholar_Lecture extends Named {






    private scholar_Teacher scholar_teacher;




    private scholar_Exam scholar_exam;


    public scholar_Lecture(
    ) {
        super(
        );
    }



    public scholar_Teacher getScholar_teacher() {
        return scholar_teacher;
    }

    public void setScholar_teacher(scholar_Teacher scholar_teacher) {
        this.scholar_teacher = scholar_teacher;
    }
    public scholar_Exam getScholar_exam() {
        return scholar_exam;
    }

    public void setScholar_exam(scholar_Exam scholar_exam) {
        this.scholar_exam = scholar_exam;
    }

}