





import java.util.List;
import java.util.ArrayList;

public class expressionDSL_StructDef extends Named, SubField, Statement {






    private List<expressionDSL_SubField> expressiondsl_subfields;


    public expressionDSL_StructDef(
    ) {
        super(
        );
        this.expressiondsl_subfields = new ArrayList<>();
    }

    public expressionDSL_StructDef(
        ArrayList<expressionDSL_SubField> expressiondsl_subfields    ) {
        this.expressiondsl_subfields = expressiondsl_subfields;
    }


    public List<expressionDSL_SubField> getExpressiondsl_subfields() {
        return expressiondsl_subfields;
    }

    public void addExpressiondsl_subfield(Expressiondsl_subfield expressiondsl_subfield) {
        this.expressiondsl_subfields.add(expressiondsl_subfield);
    }

}