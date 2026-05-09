





import java.util.List;
import java.util.ArrayList;

public class astm_RDBInsertStatement extends Statement {






    private List<astm_IncludeUnit> astm_includeunits;




    private List<astm_Expression> astm_expressions;




    private List<astm_NameSpaceDefinition> astm_namespacedefinitions;


    public astm_RDBInsertStatement(
    ) {
        super(
        );
        this.astm_includeunits = new ArrayList<>();
        this.astm_expressions = new ArrayList<>();
        this.astm_namespacedefinitions = new ArrayList<>();
    }

    public astm_RDBInsertStatement(
        ArrayList<astm_IncludeUnit> astm_includeunits,        ArrayList<astm_Expression> astm_expressions,        ArrayList<astm_NameSpaceDefinition> astm_namespacedefinitions    ) {
        this.astm_includeunits = astm_includeunits;
        this.astm_expressions = astm_expressions;
        this.astm_namespacedefinitions = astm_namespacedefinitions;
    }


    public List<astm_IncludeUnit> getAstm_includeunits() {
        return astm_includeunits;
    }

    public void addAstm_includeunit(Astm_includeunit astm_includeunit) {
        this.astm_includeunits.add(astm_includeunit);
    }
    public List<astm_Expression> getAstm_expressions() {
        return astm_expressions;
    }

    public void addAstm_expression(Astm_expression astm_expression) {
        this.astm_expressions.add(astm_expression);
    }
    public List<astm_NameSpaceDefinition> getAstm_namespacedefinitions() {
        return astm_namespacedefinitions;
    }

    public void addAstm_namespacedefinition(Astm_namespacedefinition astm_namespacedefinition) {
        this.astm_namespacedefinitions.add(astm_namespacedefinition);
    }

}