





import java.util.List;
import java.util.ArrayList;

public class myDsl_Statement  {






    private myDsl_Block mydsl_block;




    private myDsl_StatementList mydsl_statementlist;


    public myDsl_Statement(
    ) {
    }



    public myDsl_Block getMydsl_block() {
        return mydsl_block;
    }

    public void setMydsl_block(myDsl_Block mydsl_block) {
        this.mydsl_block = mydsl_block;
    }
    public myDsl_StatementList getMydsl_statementlist() {
        return mydsl_statementlist;
    }

    public void setMydsl_statementlist(myDsl_StatementList mydsl_statementlist) {
        this.mydsl_statementlist = mydsl_statementlist;
    }

}