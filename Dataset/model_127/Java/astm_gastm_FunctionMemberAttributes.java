





import java.util.List;
import java.util.ArrayList;

public class astm_gastm_FunctionMemberAttributes  {

    private boolean isFriend;
    private boolean isThisConst;
    private boolean isInline;



    public astm_gastm_FunctionMemberAttributes(
        boolean isFriend,        boolean isThisConst,        boolean isInline    ) {
        this.isFriend = isFriend;
        this.isThisConst = isThisConst;
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
    public boolean getIsinline() {
        return isInline;
    }

    public void setIsinline(boolean isInline) {
        this.isInline = isInline;
    }


}