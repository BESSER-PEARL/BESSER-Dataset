





import java.util.List;
import java.util.ArrayList;

public class ccore_ViewItemType  {

    private boolean isRootElement;
    private boolean ref;





    private ccore_ItemType ccore_itemtype;


    public ccore_ViewItemType(
        boolean isRootElement,        boolean ref    ) {
        this.isRootElement = isRootElement;
        this.ref = ref;
    }


    public boolean getIsrootelement() {
        return isRootElement;
    }

    public void setIsrootelement(boolean isRootElement) {
        this.isRootElement = isRootElement;
    }
    public boolean getRef() {
        return ref;
    }

    public void setRef(boolean ref) {
        this.ref = ref;
    }

    public ccore_ItemType getCcore_itemtype() {
        return ccore_itemtype;
    }

    public void setCcore_itemtype(ccore_ItemType ccore_itemtype) {
        this.ccore_itemtype = ccore_itemtype;
    }

}