





import java.util.List;
import java.util.ArrayList;

public class school_Course  {

    private String subject;
    private int weight;



    public school_Course(
        String subject,        int weight    ) {
        this.subject = subject;
        this.weight = weight;
    }


    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }


}