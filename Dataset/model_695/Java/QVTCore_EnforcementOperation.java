





import java.util.List;
import java.util.ArrayList;

public class QVTCore_EnforcementOperation extends Element {

    private String enforcementMode;



    public QVTCore_EnforcementOperation(
        String enforcementMode    ) {
        super(
        );
        this.enforcementMode = enforcementMode;
    }


    public String getEnforcementmode() {
        return enforcementMode;
    }

    public void setEnforcementmode(String enforcementMode) {
        this.enforcementMode = enforcementMode;
    }


}