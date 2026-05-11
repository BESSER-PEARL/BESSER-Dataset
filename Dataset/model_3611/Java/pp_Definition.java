





import java.util.List;
import java.util.ArrayList;

public class pp_Definition extends Expression {

    private String className;





    private pp_DefinitionArgumentList pp_definitionargumentlist;




    private List<pp_Expression> pp_expressions;


    public pp_Definition(
        String className    ) {
        super(
        );
        this.className = className;
        this.pp_expressions = new ArrayList<>();
    }

    public pp_Definition(
        String className        ArrayList<pp_Expression> pp_expressions    ) {
        this.className = className;
        this.pp_expressions = pp_expressions;
    }

    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }

    public pp_DefinitionArgumentList getPp_definitionargumentlist() {
        return pp_definitionargumentlist;
    }

    public void setPp_definitionargumentlist(pp_DefinitionArgumentList pp_definitionargumentlist) {
        this.pp_definitionargumentlist = pp_definitionargumentlist;
    }
    public List<pp_Expression> getPp_expressions() {
        return pp_expressions;
    }

    public void addPp_expression(Pp_expression pp_expression) {
        this.pp_expressions.add(pp_expression);
    }

}