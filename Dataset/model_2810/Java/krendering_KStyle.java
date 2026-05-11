





import java.util.List;
import java.util.ArrayList;

public class krendering_KStyle extends EMapPropertyHolder {

    private boolean selection;
    private String modifierId;
    private boolean propagateToChildren;



    public krendering_KStyle(
        boolean selection,        String modifierId,        boolean propagateToChildren    ) {
        super(
        );
        this.selection = selection;
        this.modifierId = modifierId;
        this.propagateToChildren = propagateToChildren;
    }


    public boolean getSelection() {
        return selection;
    }

    public void setSelection(boolean selection) {
        this.selection = selection;
    }
    public String getModifierid() {
        return modifierId;
    }

    public void setModifierid(String modifierId) {
        this.modifierId = modifierId;
    }
    public boolean getPropagatetochildren() {
        return propagateToChildren;
    }

    public void setPropagatetochildren(boolean propagateToChildren) {
        this.propagateToChildren = propagateToChildren;
    }


}