





import java.util.List;
import java.util.ArrayList;

public class gastm_FunctionMemberAttributes extends MinorSyntaxObject {

    private String isFriend;
    private String isInLine;
    private String isThisConst;



    public gastm_FunctionMemberAttributes(
        String isFriend,        String isInLine,        String isThisConst    ) {
        super(
        );
        this.isFriend = isFriend;
        this.isInLine = isInLine;
        this.isThisConst = isThisConst;
    }


    public String getIsfriend() {
        return isFriend;
    }

    public void setIsfriend(String isFriend) {
        this.isFriend = isFriend;
    }
    public String getIsinline() {
        return isInLine;
    }

    public void setIsinline(String isInLine) {
        this.isInLine = isInLine;
    }
    public String getIsthisconst() {
        return isThisConst;
    }

    public void setIsthisconst(String isThisConst) {
        this.isThisConst = isThisConst;
    }


}