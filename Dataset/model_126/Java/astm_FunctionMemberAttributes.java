





import java.util.List;
import java.util.ArrayList;

public class astm_FunctionMemberAttributes extends Visitable {

    private boolean isThisConst;
    private boolean isFriend;
    private boolean isInline;



    public astm_FunctionMemberAttributes(
        boolean isThisConst,        boolean isFriend,        boolean isInline    ) {
        super(
        );
        this.isThisConst = isThisConst;
        this.isFriend = isFriend;
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
    public boolean getIsinline() {
        return isInline;
    }

    public void setIsinline(boolean isInline) {
        this.isInline = isInline;
    }


}