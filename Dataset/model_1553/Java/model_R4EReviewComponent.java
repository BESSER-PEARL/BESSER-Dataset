





import java.util.List;
import java.util.ArrayList;

public class model_R4EReviewComponent extends ReviewComponent {

    private String assignedTo;



    public model_R4EReviewComponent(
        String assignedTo    ) {
        super(
        );
        this.assignedTo = assignedTo;
    }


    public String getAssignedto() {
        return assignedTo;
    }

    public void setAssignedto(String assignedTo) {
        this.assignedTo = assignedTo;
    }


}