





import java.util.List;
import java.util.ArrayList;

public class simulink_Function extends CompositeStateflowElement, ContainableStateflowElement {

    private String signature;



    public simulink_Function(
        String signature    ) {
        super(
        );
        this.signature = signature;
    }


    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }


}