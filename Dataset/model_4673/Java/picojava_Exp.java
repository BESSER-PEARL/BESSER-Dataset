





import java.util.List;
import java.util.ArrayList;

public class picojava_Exp  {

    private boolean isValue;





    private picojava_TypeDecl picojava_typedecl;




    private picojava_AssignStmt picojava_assignstmt;




    private picojava_WhileStmt picojava_whilestmt;


    public picojava_Exp(
        boolean isValue    ) {
        this.isValue = isValue;
    }


    public boolean getIsvalue() {
        return isValue;
    }

    public void setIsvalue(boolean isValue) {
        this.isValue = isValue;
    }

    public picojava_TypeDecl getPicojava_typedecl() {
        return picojava_typedecl;
    }

    public void setPicojava_typedecl(picojava_TypeDecl picojava_typedecl) {
        this.picojava_typedecl = picojava_typedecl;
    }
    public picojava_AssignStmt getPicojava_assignstmt() {
        return picojava_assignstmt;
    }

    public void setPicojava_assignstmt(picojava_AssignStmt picojava_assignstmt) {
        this.picojava_assignstmt = picojava_assignstmt;
    }
    public picojava_WhileStmt getPicojava_whilestmt() {
        return picojava_whilestmt;
    }

    public void setPicojava_whilestmt(picojava_WhileStmt picojava_whilestmt) {
        this.picojava_whilestmt = picojava_whilestmt;
    }

}