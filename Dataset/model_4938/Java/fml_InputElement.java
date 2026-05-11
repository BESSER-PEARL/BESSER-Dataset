





import java.util.List;
import java.util.ArrayList;

public class fml_InputElement extends PageElement {

    private boolean isMandatory;



    public fml_InputElement(
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