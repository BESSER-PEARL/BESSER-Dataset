





import java.util.List;
import java.util.ArrayList;

public class Question  {






    private List<Exam> exams;


    public Question(
    ) {
        this.exams = new ArrayList<>();
    }

    public Question(
        ArrayList<Exam> exams    ) {
        this.exams = exams;
    }


    public List<Exam> getExams() {
        return exams;
    }

    public void addExam(Exam exam) {
        this.exams.add(exam);
    }

}