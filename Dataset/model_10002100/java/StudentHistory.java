





import java.util.List;
import java.util.ArrayList;

public class StudentHistory  {

    private None student;
    private None activity;
    private int sequence;





    private Activity activity;


    public StudentHistory(
        None student,        None activity,        int sequence    ) {
        this.student = student;
        this.activity = activity;
        this.sequence = sequence;
    }


    public None getStudent() {
        return student;
    }

    public void setStudent(None student) {
        this.student = student;
    }
    public None getActivity() {
        return activity;
    }

    public void setActivity(None activity) {
        this.activity = activity;
    }
    public int getSequence() {
        return sequence;
    }

    public void setSequence(int sequence) {
        this.sequence = sequence;
    }

    public Activity getActivity() {
        return activity;
    }

    public void setActivity(Activity activity) {
        this.activity = activity;
    }

}