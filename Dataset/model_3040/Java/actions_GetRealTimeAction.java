





import java.util.List;
import java.util.ArrayList;

public class actions_GetRealTimeAction extends DependentAction, PreGenerationAction {

    private String timeHint;



    public actions_GetRealTimeAction(
        String timeHint    ) {
        super(
        );
        this.timeHint = timeHint;
    }


    public String getTimehint() {
        return timeHint;
    }

    public void setTimehint(String timeHint) {
        this.timeHint = timeHint;
    }


}