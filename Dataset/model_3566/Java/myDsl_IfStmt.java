





import java.util.List;
import java.util.ArrayList;

public class myDsl_IfStmt  {

    private String if_;
    private String else_;





    private myDsl_Statement mydsl_statement;




    private myDsl_Block mydsl_block;




    private myDsl_Expression mydsl_expression;




    private myDsl_IfStmt mydsl_ifstmt;




    private myDsl_Block mydsl_block;




    private myDsl_ShortVarDecl mydsl_shortvardecl;


    public myDsl_IfStmt(
        String if_,        String else_    ) {
        this.if_ = if_;
        this.else_ = else_;
    }


    public String getIf_() {
        return if_;
    }

    public void setIf_(String if_) {
        this.if_ = if_;
    }
    public String getElse_() {
        return else_;
    }

    public void setElse_(String else_) {
        this.else_ = else_;
    }

    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }
    public myDsl_Block getMydsl_block() {
        return mydsl_block;
    }

    public void setMydsl_block(myDsl_Block mydsl_block) {
        this.mydsl_block = mydsl_block;
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_IfStmt getMydsl_ifstmt() {
        return mydsl_ifstmt;
    }

    public void setMydsl_ifstmt(myDsl_IfStmt mydsl_ifstmt) {
        this.mydsl_ifstmt = mydsl_ifstmt;
    }
    public myDsl_Block getMydsl_block() {
        return mydsl_block;
    }

    public void setMydsl_block(myDsl_Block mydsl_block) {
        this.mydsl_block = mydsl_block;
    }
    public myDsl_ShortVarDecl getMydsl_shortvardecl() {
        return mydsl_shortvardecl;
    }

    public void setMydsl_shortvardecl(myDsl_ShortVarDecl mydsl_shortvardecl) {
        this.mydsl_shortvardecl = mydsl_shortvardecl;
    }

}