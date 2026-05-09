





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_Helper extends ATL_Callable, ATL_ModuleElement {

    private String isAttribute;
    private boolean hasContext;



    public atlext_ATL_Helper(
        String isAttribute,        boolean hasContext    ) {
        super(
        );
        this.isAttribute = isAttribute;
        this.hasContext = hasContext;
    }


    public String getIsattribute() {
        return isAttribute;
    }

    public void setIsattribute(String isAttribute) {
        this.isAttribute = isAttribute;
    }
    public boolean getHascontext() {
        return hasContext;
    }

    public void setHascontext(boolean hasContext) {
        this.hasContext = hasContext;
    }


}