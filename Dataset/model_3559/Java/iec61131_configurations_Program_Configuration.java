





import java.util.List;
import java.util.ArrayList;

public class iec61131_configurations_Program_Configuration extends Commentable {

    private boolean retain;



    public iec61131_configurations_Program_Configuration(
        boolean retain    ) {
        super(
        );
        this.retain = retain;
    }


    public boolean getRetain() {
        return retain;
    }

    public void setRetain(boolean retain) {
        this.retain = retain;
    }


}