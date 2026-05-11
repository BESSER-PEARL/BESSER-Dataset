





import java.util.List;
import java.util.ArrayList;

public class myDsl_SelectStmt  {

    private String select;





    private myDsl_Statement mydsl_statement;


    public myDsl_SelectStmt(
        String select    ) {
        this.select = select;
    }


    public String getSelect() {
        return select;
    }

    public void setSelect(String select) {
        this.select = select;
    }

    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}