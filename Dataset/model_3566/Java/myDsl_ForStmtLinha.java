





import java.util.List;
import java.util.ArrayList;

public class myDsl_ForStmtLinha  {

    private String vazio;





    private List<myDsl_Expression> mydsl_expressions;




    private myDsl_Expression mydsl_expression;




    private myDsl_ForStmt mydsl_forstmt;


    public myDsl_ForStmtLinha(
        String vazio    ) {
        this.vazio = vazio;
        this.mydsl_expressions = new ArrayList<>();
    }

    public myDsl_ForStmtLinha(
        String vazio        ArrayList<myDsl_Expression> mydsl_expressions    ) {
        this.vazio = vazio;
        this.mydsl_expressions = mydsl_expressions;
    }

    public String getVazio() {
        return vazio;
    }

    public void setVazio(String vazio) {
        this.vazio = vazio;
    }

    public List<myDsl_Expression> getMydsl_expressions() {
        return mydsl_expressions;
    }

    public void addMydsl_expression(Mydsl_expression mydsl_expression) {
        this.mydsl_expressions.add(mydsl_expression);
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_ForStmt getMydsl_forstmt() {
        return mydsl_forstmt;
    }

    public void setMydsl_forstmt(myDsl_ForStmt mydsl_forstmt) {
        this.mydsl_forstmt = mydsl_forstmt;
    }

}