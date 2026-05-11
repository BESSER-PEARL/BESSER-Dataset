





import java.util.List;
import java.util.ArrayList;

public class pp1_ResourceExpression extends Expression {






    private List<pp1_ResourceBody> pp1_resourcebodys;




    private pp1_Expression pp1_expression;


    public pp1_ResourceExpression(
    ) {
        super(
        );
        this.pp1_resourcebodys = new ArrayList<>();
    }

    public pp1_ResourceExpression(
        ArrayList<pp1_ResourceBody> pp1_resourcebodys    ) {
        this.pp1_resourcebodys = pp1_resourcebodys;
    }


    public List<pp1_ResourceBody> getPp1_resourcebodys() {
        return pp1_resourcebodys;
    }

    public void addPp1_resourcebody(Pp1_resourcebody pp1_resourcebody) {
        this.pp1_resourcebodys.add(pp1_resourcebody);
    }
    public pp1_Expression getPp1_expression() {
        return pp1_expression;
    }

    public void setPp1_expression(pp1_Expression pp1_expression) {
        this.pp1_expression = pp1_expression;
    }

}