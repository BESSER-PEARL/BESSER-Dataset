





import java.util.List;
import java.util.ArrayList;

public class krendering_KStyle extends EMapPropertyHolder {

    private String modifierId;
    private boolean propagateToChildren;
    private boolean selection;



    public krendering_KStyle(
        String modifierId,        boolean propagateToChildren,        boolean selection    ) {
        super(
        );
        this.modifierId = modifierId;
        this.propagateToChildren = propagateToChildren;
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
    public boolean getSelection() {
        return selection;
    }

    public void setSelection(boolean selection) {
        this.selection = selection;
    }


}