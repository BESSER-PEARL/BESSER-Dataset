





import java.util.List;
import java.util.ArrayList;

public class uma_WorkDefinition extends MethodElement {

    private String postcondition;
    private String precondition;



    public uma_WorkDefinition(
        String postcondition,        String precondition    ) {
        super(
        );
        this.postcondition = postcondition;
        this.precondition = precondition;
    }


    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }


}