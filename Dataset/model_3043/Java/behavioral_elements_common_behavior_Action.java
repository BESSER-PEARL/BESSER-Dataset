





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_common_behavior_Action extends ModelElement {

    private String isAsynchronous;



    public behavioral_elements_common_behavior_Action(
        String isAsynchronous    ) {
        super(
        );
        this.isAsynchronous = isAsynchronous;
    }


    public String getIsasynchronous() {
        return isAsynchronous;
    }

    public void setIsasynchronous(String isAsynchronous) {
        this.isAsynchronous = isAsynchronous;
    }


}