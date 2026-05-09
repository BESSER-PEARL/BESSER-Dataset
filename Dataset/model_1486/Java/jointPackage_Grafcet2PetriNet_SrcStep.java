





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Grafcet2PetriNet_SrcStep extends SrcElement {

    private boolean isActive;
    private String action;
    private boolean isInitial;



    public jointPackage_Grafcet2PetriNet_SrcStep(
        boolean isActive,        String action,        boolean isInitial    ) {
        super(
        );
        this.isActive = isActive;
        this.action = action;
        this.isInitial = isInitial;
    }


    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }


}