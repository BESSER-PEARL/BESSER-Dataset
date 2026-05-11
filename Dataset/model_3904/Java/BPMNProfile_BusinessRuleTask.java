





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BusinessRuleTask extends Task {

    private String implementation;



    public BPMNProfile_BusinessRuleTask(
        String implementation    ) {
        super(
        );
        this.implementation = implementation;
    }


    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }


}