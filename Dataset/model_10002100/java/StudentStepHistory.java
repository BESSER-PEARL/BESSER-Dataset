





import java.util.List;
import java.util.ArrayList;

public class StudentStepHistory  {

    private boolean status;
    private None student;
    private int tries;
    private None step;





    private Step step;


    public StudentStepHistory(
        boolean status,        None student,        int tries,        None step    ) {
        this.status = status;
        this.student = student;
        this.tries = tries;
        this.step = step;
    }


    public boolean getStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }
    public None getStudent() {
        return student;
    }

    public void setStudent(None student) {
        this.student = student;
    }
    public int getTries() {
        return tries;
    }

    public void setTries(int tries) {
        this.tries = tries;
    }
    public None getStep() {
        return step;
    }

    public void setStep(None step) {
        this.step = step;
    }

    public Step getStep() {
        return step;
    }

    public void setStep(Step step) {
        this.step = step;
    }

}