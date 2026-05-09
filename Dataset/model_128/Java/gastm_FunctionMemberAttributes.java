





import java.util.List;
import java.util.ArrayList;

public class gastm_FunctionMemberAttributes  {

    private boolean isThisConst;
    private boolean isInline;
    private boolean isFriend;



    public gastm_FunctionMemberAttributes(
        boolean isThisConst,        boolean isInline,        boolean isFriend    ) {
        this.isThisConst = isThisConst;
        this.isInline = isInline;
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
    public boolean getIsfriend() {
        return isFriend;
    }

    public void setIsfriend(boolean isFriend) {
        this.isFriend = isFriend;
    }


}