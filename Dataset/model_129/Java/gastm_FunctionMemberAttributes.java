





import java.util.List;
import java.util.ArrayList;

public class gastm_FunctionMemberAttributes  {

    private boolean isInline;
    private boolean isFriend;
    private boolean isThisConst;





    private VirtualSpecification virtualspecification;


    public gastm_FunctionMemberAttributes(
        boolean isInline,        boolean isFriend,        boolean isThisConst    ) {
        this.isInline = isInline;
        this.isFriend = isFriend;
        this.isThisConst = isThisConst;
    }


    public boolean getIsinline() {
        return isInline;
    }

    public void setIsinline(boolean isInline) {
        this.isInline = isInline;
    }
    public boolean getIsfriend() {
        return isFriend;
    }

    public void setIsfriend(boolean isFriend) {
        this.isFriend = isFriend;
    }
    public boolean getIsthisconst() {
        return isThisConst;
    }

    public void setIsthisconst(boolean isThisConst) {
        this.isThisConst = isThisConst;
    }

    public VirtualSpecification getVirtualspecification() {
        return virtualspecification;
    }

    public void setVirtualspecification(VirtualSpecification virtualspecification) {
        this.virtualspecification = virtualspecification;
    }

}