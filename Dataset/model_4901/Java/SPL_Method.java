





import java.util.List;
import java.util.ArrayList;

public class SPL_Method extends Session {

    private String direction;





    private List<SPL_Statement> spl_statements;




    private SPL_MethodName spl_methodname;




    private List<SPL_Branch> spl_branchs;




    private SPL_TypeExpression spl_typeexpression;


    public SPL_Method(
        String direction    ) {
        super(
        );
        this.direction = direction;
        this.spl_statements = new ArrayList<>();
        this.spl_branchs = new ArrayList<>();
    }

    public SPL_Method(
        String direction        ArrayList<SPL_Statement> spl_statements,        ArrayList<SPL_Branch> spl_branchs    ) {
        this.direction = direction;
        this.spl_statements = spl_statements;
        this.spl_branchs = spl_branchs;
    }

    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public List<SPL_Statement> getSpl_statements() {
        return spl_statements;
    }

    public void addSpl_statement(Spl_statement spl_statement) {
        this.spl_statements.add(spl_statement);
    }
    public SPL_MethodName getSpl_methodname() {
        return spl_methodname;
    }

    public void setSpl_methodname(SPL_MethodName spl_methodname) {
        this.spl_methodname = spl_methodname;
    }
    public List<SPL_Branch> getSpl_branchs() {
        return spl_branchs;
    }

    public void addSpl_branch(Spl_branch spl_branch) {
        this.spl_branchs.add(spl_branch);
    }
    public SPL_TypeExpression getSpl_typeexpression() {
        return spl_typeexpression;
    }

    public void setSpl_typeexpression(SPL_TypeExpression spl_typeexpression) {
        this.spl_typeexpression = spl_typeexpression;
    }

}