





import java.util.List;
import java.util.ArrayList;

public class myDsl_ForStmt  {

    private String for_;
    private String range;





    private myDsl_ShortVarDecl mydsl_shortvardecl;




    private myDsl_Expression mydsl_expression;




    private myDsl_IdentifierList mydsl_identifierlist;




    private myDsl_Statement mydsl_statement;




    private myDsl_Block mydsl_block;


    public myDsl_ForStmt(
        String for_,        String range    ) {
        this.for_ = for_;
        this.range = range;
    }


    public String getFor_() {
        return for_;
    }

    public void setFor_(String for_) {
        this.for_ = for_;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }

    public myDsl_ShortVarDecl getMydsl_shortvardecl() {
        return mydsl_shortvardecl;
    }

    public void setMydsl_shortvardecl(myDsl_ShortVarDecl mydsl_shortvardecl) {
        this.mydsl_shortvardecl = mydsl_shortvardecl;
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_IdentifierList getMydsl_identifierlist() {
        return mydsl_identifierlist;
    }

    public void setMydsl_identifierlist(myDsl_IdentifierList mydsl_identifierlist) {
        this.mydsl_identifierlist = mydsl_identifierlist;
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

}