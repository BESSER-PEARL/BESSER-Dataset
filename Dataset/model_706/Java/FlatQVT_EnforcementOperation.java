





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_EnforcementOperation extends Element {

    private String enforcementMode;





    private BottomPattern bottompattern;


    public FlatQVT_EnforcementOperation(
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

    public BottomPattern getBottompattern() {
        return bottompattern;
    }

    public void setBottompattern(BottomPattern bottompattern) {
        this.bottompattern = bottompattern;
    }

}