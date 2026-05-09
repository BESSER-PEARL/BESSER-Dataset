





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ProtocolTransition extends Transition {

    private String referred;
    private String postCondition;
    private String preCondition;



    public UMLModel_ProtocolTransition(
        String referred,        String postCondition,        String preCondition    ) {
        super(
        );
        this.referred = referred;
        this.postCondition = postCondition;
        this.preCondition = preCondition;
    }


    public String getReferred() {
        return referred;
    }

    public void setReferred(String referred) {
        this.referred = referred;
    }
    public String getPostcondition() {
        return postCondition;
    }

    public void setPostcondition(String postCondition) {
        this.postCondition = postCondition;
    }
    public String getPrecondition() {
        return preCondition;
    }

    public void setPrecondition(String preCondition) {
        this.preCondition = preCondition;
    }


}