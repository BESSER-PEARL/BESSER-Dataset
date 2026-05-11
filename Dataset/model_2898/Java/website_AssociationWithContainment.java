





import java.util.List;
import java.util.ArrayList;

public class website_AssociationWithContainment extends EntityAssociation {

    private boolean sourceVisible;



    public website_AssociationWithContainment(
        boolean sourceVisible    ) {
        super(
        );
        this.sourceVisible = sourceVisible;
    }


    public boolean getSourcevisible() {
        return sourceVisible;
    }

    public void setSourcevisible(boolean sourceVisible) {
        this.sourceVisible = sourceVisible;
    }


}