





import java.util.List;
import java.util.ArrayList;

public class myDsl_Try_statement  {

    private String lParen;
    private String rparent;





    private List<myDsl_Parameter> mydsl_parameters;




    private myDsl_Statement mydsl_statement;




    private List<myDsl_Statement> mydsl_statements;




    private myDsl_Statement mydsl_statement;




    private myDsl_Statement mydsl_statement;


    public myDsl_Try_statement(
        String lParen,        String rparent    ) {
        this.lParen = lParen;
        this.rparent = rparent;
        this.mydsl_parameters = new ArrayList<>();
        this.mydsl_statements = new ArrayList<>();
    }

    public myDsl_Try_statement(
        String lParen,        String rparent        ArrayList<myDsl_Parameter> mydsl_parameters,        ArrayList<myDsl_Statement> mydsl_statements    ) {
        this.lParen = lParen;
        this.rparent = rparent;
        this.mydsl_parameters = mydsl_parameters;
        this.mydsl_statements = mydsl_statements;
    }

    public String getLparen() {
        return lParen;
    }

    public void setLparen(String lParen) {
        this.lParen = lParen;
    }
    public String getRparent() {
        return rparent;
    }

    public void setRparent(String rparent) {
        this.rparent = rparent;
    }

    public List<myDsl_Parameter> getMydsl_parameters() {
        return mydsl_parameters;
    }

    public void addMydsl_parameter(Mydsl_parameter mydsl_parameter) {
        this.mydsl_parameters.add(mydsl_parameter);
    }
    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }
    public List<myDsl_Statement> getMydsl_statements() {
        return mydsl_statements;
    }

    public void addMydsl_statement(Mydsl_statement mydsl_statement) {
        this.mydsl_statements.add(mydsl_statement);
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