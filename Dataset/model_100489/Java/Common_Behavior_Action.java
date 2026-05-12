





import java.util.List;
import java.util.ArrayList;

public class Common_Behavior_Action extends ModelElement {

    private String isAsynchronous;



    public Common_Behavior_Action(
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