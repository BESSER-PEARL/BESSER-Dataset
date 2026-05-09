





import java.util.List;
import java.util.ArrayList;

public class gastm_FunctionMemberAttributes  {

    private boolean isInline;
    private boolean isThisConst;
    private boolean isFriend;



    public gastm_FunctionMemberAttributes(
        boolean isInline,        boolean isThisConst,        boolean isFriend    ) {
        this.isInline = isInline;
        this.isThisConst = isThisConst;
        this.isFriend = isFriend;
    }


    public boolean getIsinline() {
        return isInline;
    }

    public void setIsinline(boolean isInline) {
        this.isInline = isInline;
    }
    public boolean getIsthisconst() {
        return isThisConst;
    }

    public void setIsthisconst(boolean isThisConst) {
        this.isThisConst = isThisConst;
    }
    public boolean getIsfriend() {
        return isFriend;
    }

    public void setIsfriend(boolean isFriend) {
        this.isFriend = isFriend;
    }


}