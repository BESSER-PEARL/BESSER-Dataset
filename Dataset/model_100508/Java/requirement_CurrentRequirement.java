





import java.util.List;
import java.util.ArrayList;

public class requirement_CurrentRequirement extends Requirement {

    private boolean impacted;



    public requirement_CurrentRequirement(
        boolean impacted    ) {
        super(
        );
        this.impacted = impacted;
    }


    public boolean getImpacted() {
        return impacted;
    }

    public void setImpacted(boolean impacted) {
        this.impacted = impacted;
    }


}