





import java.util.List;
import java.util.ArrayList;

public class persistence_AssociationWithContainment extends Association {

    private boolean sourceVisible;



    public persistence_AssociationWithContainment(
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