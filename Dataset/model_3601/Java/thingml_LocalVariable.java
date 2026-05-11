





import java.util.List;
import java.util.ArrayList;

public class thingml_LocalVariable extends Variable, Action {

    private boolean changeable;



    public thingml_LocalVariable(
        boolean changeable    ) {
        super(
        );
        this.changeable = changeable;
    }


    public boolean getChangeable() {
        return changeable;
    }

    public void setChangeable(boolean changeable) {
        this.changeable = changeable;
    }


}