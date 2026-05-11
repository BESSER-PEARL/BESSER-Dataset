





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_RequiredPort extends Port {

    private boolean isMandatory;



    public cloudml_core_RequiredPort(
        boolean isMandatory    ) {
        super(
        );
        this.isMandatory = isMandatory;
    }


    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }


}