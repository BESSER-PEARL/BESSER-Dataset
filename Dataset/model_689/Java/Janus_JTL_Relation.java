





import java.util.List;
import java.util.ArrayList;

public class Janus_JTL_Relation extends NamedElement {

    private boolean isTopLevel;



    public Janus_JTL_Relation(
        boolean isTopLevel    ) {
        super(
        );
        this.isTopLevel = isTopLevel;
    }


    public boolean getIstoplevel() {
        return isTopLevel;
    }

    public void setIstoplevel(boolean isTopLevel) {
        this.isTopLevel = isTopLevel;
    }


}