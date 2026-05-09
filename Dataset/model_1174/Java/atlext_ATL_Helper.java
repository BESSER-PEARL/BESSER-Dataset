





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_Helper extends ATL_Callable, ATL_ModuleElement {

    private boolean hasContext;
    private boolean isAttribute;



    public atlext_ATL_Helper(
        boolean hasContext,        boolean isAttribute    ) {
        super(
        );
        this.hasContext = hasContext;
        this.isAttribute = isAttribute;
    }


    public boolean getHascontext() {
        return hasContext;
    }

    public void setHascontext(boolean hasContext) {
        this.hasContext = hasContext;
    }
    public boolean getIsattribute() {
        return isAttribute;
    }

    public void setIsattribute(boolean isAttribute) {
        this.isAttribute = isAttribute;
    }


}