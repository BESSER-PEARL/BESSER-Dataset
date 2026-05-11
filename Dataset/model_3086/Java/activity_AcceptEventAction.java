





import java.util.List;
import java.util.ArrayList;

public class activity_AcceptEventAction extends AbstractAction {

    private boolean isUnmarshall;



    public activity_AcceptEventAction(
        boolean isUnmarshall    ) {
        super(
        );
        this.isUnmarshall = isUnmarshall;
    }


    public boolean getIsunmarshall() {
        return isUnmarshall;
    }

    public void setIsunmarshall(boolean isUnmarshall) {
        this.isUnmarshall = isUnmarshall;
    }


}