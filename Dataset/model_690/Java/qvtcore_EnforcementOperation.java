





import java.util.List;
import java.util.ArrayList;

public class qvtcore_EnforcementOperation  {

    private String enforcementMode;





    private OperationCallExp operationcallexp;




    private BottomPattern bottompattern;


    public qvtcore_EnforcementOperation(
        String enforcementMode    ) {
        this.enforcementMode = enforcementMode;
    }


    public String getEnforcementmode() {
        return enforcementMode;
    }

    public void setEnforcementmode(String enforcementMode) {
        this.enforcementMode = enforcementMode;
    }

    public OperationCallExp getOperationcallexp() {
        return operationcallexp;
    }

    public void setOperationcallexp(OperationCallExp operationcallexp) {
        this.operationcallexp = operationcallexp;
    }
    public BottomPattern getBottompattern() {
        return bottompattern;
    }

    public void setBottompattern(BottomPattern bottompattern) {
        this.bottompattern = bottompattern;
    }

}