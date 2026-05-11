





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_GlobalBusinessRuleTask extends GlobalTask {

    private String implementation;



    public BPMNProfile_GlobalBusinessRuleTask(
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