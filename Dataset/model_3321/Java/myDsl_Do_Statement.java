





import java.util.List;
import java.util.ArrayList;

public class myDsl_Do_Statement  {

    private String lparent;
    private String rparent;





    private myDsl_Statement mydsl_statement;




    private myDsl_Statement mydsl_statement;


    public myDsl_Do_Statement(
        String lparent,        String rparent    ) {
        this.lparent = lparent;
        this.rparent = rparent;
    }


    public String getLparent() {
        return lparent;
    }

    public void setLparent(String lparent) {
        this.lparent = lparent;
    }
    public String getRparent() {
        return rparent;
    }

    public void setRparent(String rparent) {
        this.rparent = rparent;
    }

    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }
    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}