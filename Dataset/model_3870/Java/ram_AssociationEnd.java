





import java.util.List;
import java.util.ArrayList;

public class ram_AssociationEnd extends Property {

    private boolean navigable;



    public ram_AssociationEnd(
        boolean navigable    ) {
        super(
        );
        this.navigable = navigable;
    }


    public boolean getNavigable() {
        return navigable;
    }

    public void setNavigable(boolean navigable) {
        this.navigable = navigable;
    }


}