





import java.util.List;
import java.util.ArrayList;

public class company_Freelance extends Employee {

    private String assignment;



    public company_Freelance(
        String assignment    ) {
        super(
        );
        this.assignment = assignment;
    }


    public String getAssignment() {
        return assignment;
    }

    public void setAssignment(String assignment) {
        this.assignment = assignment;
    }


}