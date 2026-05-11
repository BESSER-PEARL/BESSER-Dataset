





import java.util.List;
import java.util.ArrayList;

public class myDsl_TypeSwitchGuard  {

    private String type;
    private String id;





    private myDsl_TypeSwitchStmt mydsl_typeswitchstmt;




    private myDsl_PrimaryExpr mydsl_primaryexpr;


    public myDsl_TypeSwitchGuard(
        String type,        String id    ) {
        this.type = type;
        this.id = id;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_TypeSwitchStmt getMydsl_typeswitchstmt() {
        return mydsl_typeswitchstmt;
    }

    public void setMydsl_typeswitchstmt(myDsl_TypeSwitchStmt mydsl_typeswitchstmt) {
        this.mydsl_typeswitchstmt = mydsl_typeswitchstmt;
    }
    public myDsl_PrimaryExpr getMydsl_primaryexpr() {
        return mydsl_primaryexpr;
    }

    public void setMydsl_primaryexpr(myDsl_PrimaryExpr mydsl_primaryexpr) {
        this.mydsl_primaryexpr = mydsl_primaryexpr;
    }

}