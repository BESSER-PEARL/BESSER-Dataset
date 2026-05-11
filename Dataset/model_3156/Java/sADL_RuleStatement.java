





import java.util.List;
import java.util.ArrayList;

public class sADL_RuleStatement extends ExpressionScope {






    private sADL_SadlResource sadl_sadlresource;




    private List<sADL_Expression> sadl_expressions;




    private List<sADL_NamedStructureAnnotation> sadl_namedstructureannotations;




    private List<sADL_Expression> sadl_expressions;


    public sADL_RuleStatement(
    ) {
        super(
        );
        this.sadl_expressions = new ArrayList<>();
        this.sadl_namedstructureannotations = new ArrayList<>();
        this.sadl_expressions = new ArrayList<>();
    }

    public sADL_RuleStatement(
        ArrayList<sADL_Expression> sadl_expressions,        ArrayList<sADL_NamedStructureAnnotation> sadl_namedstructureannotations,        ArrayList<sADL_Expression> sadl_expressions    ) {
        this.sadl_expressions = sadl_expressions;
        this.sadl_namedstructureannotations = sadl_namedstructureannotations;
        this.sadl_expressions = sadl_expressions;
    }


    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }
    public List<sADL_Expression> getSadl_expressions() {
        return sadl_expressions;
    }

    public void addSadl_expression(Sadl_expression sadl_expression) {
        this.sadl_expressions.add(sadl_expression);
    }
    public List<sADL_NamedStructureAnnotation> getSadl_namedstructureannotations() {
        return sadl_namedstructureannotations;
    }

    public void addSadl_namedstructureannotation(Sadl_namedstructureannotation sadl_namedstructureannotation) {
        this.sadl_namedstructureannotations.add(sadl_namedstructureannotation);
    }
    public List<sADL_Expression> getSadl_expressions() {
        return sadl_expressions;
    }

    public void addSadl_expression(Sadl_expression sadl_expression) {
        this.sadl_expressions.add(sadl_expression);
    }

}