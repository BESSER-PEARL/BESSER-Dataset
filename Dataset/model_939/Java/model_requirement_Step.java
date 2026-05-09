





import java.util.List;
import java.util.ArrayList;

public class model_requirement_Step extends UnicaseModelElement, NonDomainElement {

    private boolean userStep;



    public model_requirement_Step(
        boolean userStep    ) {
        super(
        );
        this.userStep = userStep;
    }


    public boolean getUserstep() {
        return userStep;
    }

    public void setUserstep(boolean userStep) {
        this.userStep = userStep;
    }


}