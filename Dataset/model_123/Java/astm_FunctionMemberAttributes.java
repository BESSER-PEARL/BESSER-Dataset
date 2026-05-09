





import java.util.List;
import java.util.ArrayList;

public class astm_FunctionMemberAttributes  {

    private boolean isFriend;
    private boolean isInline;
    private boolean isThisConst;





    private astm_FunctionDeclaration astm_functiondeclaration;




    private astm_VirtualSpecification astm_virtualspecification;


    public astm_FunctionMemberAttributes(
        boolean isFriend,        boolean isInline,        boolean isThisConst    ) {
        this.isFriend = isFriend;
        this.isInline = isInline;
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
    public boolean getIsthisconst() {
        return isThisConst;
    }

    public void setIsthisconst(boolean isThisConst) {
        this.isThisConst = isThisConst;
    }

    public astm_FunctionDeclaration getAstm_functiondeclaration() {
        return astm_functiondeclaration;
    }

    public void setAstm_functiondeclaration(astm_FunctionDeclaration astm_functiondeclaration) {
        this.astm_functiondeclaration = astm_functiondeclaration;
    }
    public astm_VirtualSpecification getAstm_virtualspecification() {
        return astm_virtualspecification;
    }

    public void setAstm_virtualspecification(astm_VirtualSpecification astm_virtualspecification) {
        this.astm_virtualspecification = astm_virtualspecification;
    }

}