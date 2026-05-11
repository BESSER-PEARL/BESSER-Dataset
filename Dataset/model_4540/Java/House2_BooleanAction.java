





import java.util.List;
import java.util.ArrayList;

public class House2_BooleanAction extends Action {

    private boolean switchTo;



    public House2_BooleanAction(
        boolean switchTo    ) {
        super(
        );
        this.switchTo = switchTo;
    }


    public boolean getSwitchto() {
        return switchTo;
    }

    public void setSwitchto(boolean switchTo) {
        this.switchTo = switchTo;
    }


}