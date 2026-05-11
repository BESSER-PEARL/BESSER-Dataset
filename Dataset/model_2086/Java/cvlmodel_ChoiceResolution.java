





import java.util.List;
import java.util.ArrayList;

public class cvlmodel_ChoiceResolution extends VSpecResolution {

    private String decision;



    public cvlmodel_ChoiceResolution(
        String decision    ) {
        super(
        );
        this.decision = decision;
    }


    public String getDecision() {
        return decision;
    }

    public void setDecision(String decision) {
        this.decision = decision;
    }


}