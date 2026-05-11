





import java.util.List;
import java.util.ArrayList;

public class school_Course  {

    private int weight;
    private String subject;



    public school_Course(
        int weight,        String subject    ) {
        this.weight = weight;
        this.subject = subject;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }


}