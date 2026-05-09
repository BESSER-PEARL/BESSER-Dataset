





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_LinkEndCreationData extends LinkEndData {

    private boolean isReplaceAll;





    private UML2WithID_InputPin uml2withid_inputpin;


    public UML2WithID_LinkEndCreationData(
        boolean isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
    }


    public boolean getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(boolean isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }

    public UML2WithID_InputPin getUml2withid_inputpin() {
        return uml2withid_inputpin;
    }

    public void setUml2withid_inputpin(UML2WithID_InputPin uml2withid_inputpin) {
        this.uml2withid_inputpin = uml2withid_inputpin;
    }

}