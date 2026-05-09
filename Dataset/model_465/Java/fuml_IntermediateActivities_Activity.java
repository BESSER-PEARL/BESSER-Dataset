





import java.util.List;
import java.util.ArrayList;

public class fuml_IntermediateActivities_Activity extends Behavior {

    private boolean readOnly;



    public fuml_IntermediateActivities_Activity(
        boolean readOnly    ) {
        super(
        );
        this.readOnly = readOnly;
    }


    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }


}