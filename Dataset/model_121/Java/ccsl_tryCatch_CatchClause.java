





import java.util.List;
import java.util.ArrayList;

public class ccsl_tryCatch_CatchClause extends Statement {






    private List<complexType_JClass> complextype_jclasss;




    private variable_ParameterVariable variable_parametervariable;


    public ccsl_tryCatch_CatchClause(
    ) {
        super(
        );
        this.complextype_jclasss = new ArrayList<>();
    }

    public ccsl_tryCatch_CatchClause(
        ArrayList<complexType_JClass> complextype_jclasss    ) {
        this.complextype_jclasss = complextype_jclasss;
    }


    public List<complexType_JClass> getComplextype_jclasss() {
        return complextype_jclasss;
    }

    public void addComplextype_jclass(Complextype_jclass complextype_jclass) {
        this.complextype_jclasss.add(complextype_jclass);
    }
    public variable_ParameterVariable getVariable_parametervariable() {
        return variable_parametervariable;
    }

    public void setVariable_parametervariable(variable_ParameterVariable variable_parametervariable) {
        this.variable_parametervariable = variable_parametervariable;
    }

}