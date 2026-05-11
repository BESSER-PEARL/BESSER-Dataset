





import java.util.List;
import java.util.ArrayList;

public class pp_ResourceExpression extends Expression {






    private pp_Expression pp_expression;




    private List<pp_ResourceBody> pp_resourcebodys;


    public pp_ResourceExpression(
    ) {
        super(
        );
        this.pp_resourcebodys = new ArrayList<>();
    }

    public pp_ResourceExpression(
        ArrayList<pp_ResourceBody> pp_resourcebodys    ) {
        this.pp_resourcebodys = pp_resourcebodys;
    }


    public pp_Expression getPp_expression() {
        return pp_expression;
    }

    public void setPp_expression(pp_Expression pp_expression) {
        this.pp_expression = pp_expression;
    }
    public List<pp_ResourceBody> getPp_resourcebodys() {
        return pp_resourcebodys;
    }

    public void addPp_resourcebody(Pp_resourcebody pp_resourcebody) {
        this.pp_resourcebodys.add(pp_resourcebody);
    }

}