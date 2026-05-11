





import java.util.List;
import java.util.ArrayList;

public class camel_deployment_RequiredCommunication extends CommunicationPort {

    private boolean isMandatory;



    public camel_deployment_RequiredCommunication(
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