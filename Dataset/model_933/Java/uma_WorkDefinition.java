





import java.util.List;
import java.util.ArrayList;

public class uma_WorkDefinition extends MethodElement {

    private String precondition;
    private String postcondition;



    public uma_WorkDefinition(
        String precondition,        String postcondition    ) {
        super(
        );
        this.precondition = precondition;
        this.postcondition = postcondition;
    }


    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }


}