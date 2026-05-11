





import java.util.List;
import java.util.ArrayList;

public class asmeta_structure_FunctionDefinition  {






    private Function function;




    private List<basicterms_VariableTerm> basicterms_variableterms;




    private basicterms_Term basicterms_term;


    public asmeta_structure_FunctionDefinition(
    ) {
        this.basicterms_variableterms = new ArrayList<>();
    }

    public asmeta_structure_FunctionDefinition(
        ArrayList<basicterms_VariableTerm> basicterms_variableterms    ) {
        this.basicterms_variableterms = basicterms_variableterms;
    }


    public Function getFunction() {
        return function;
    }

    public void setFunction(Function function) {
        this.function = function;
    }
    public List<basicterms_VariableTerm> getBasicterms_variableterms() {
        return basicterms_variableterms;
    }

    public void addBasicterms_variableterm(Basicterms_variableterm basicterms_variableterm) {
        this.basicterms_variableterms.add(basicterms_variableterm);
    }
    public basicterms_Term getBasicterms_term() {
        return basicterms_term;
    }

    public void setBasicterms_term(basicterms_Term basicterms_term) {
        this.basicterms_term = basicterms_term;
    }

}