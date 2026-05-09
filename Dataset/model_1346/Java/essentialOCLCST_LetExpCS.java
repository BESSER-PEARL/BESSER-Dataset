





import java.util.List;
import java.util.ArrayList;

public class essentialOCLCST_LetExpCS extends OclExpressionCS {






    private essentialOCLCST_OclExpressionCS essentialoclcst_oclexpressioncs;




    private List<essentialOCLCST_VariableCS> essentialoclcst_variablecss;


    public essentialOCLCST_LetExpCS(
    ) {
        super(
        );
        this.essentialoclcst_variablecss = new ArrayList<>();
    }

    public essentialOCLCST_LetExpCS(
        ArrayList<essentialOCLCST_VariableCS> essentialoclcst_variablecss    ) {
        this.essentialoclcst_variablecss = essentialoclcst_variablecss;
    }


    public essentialOCLCST_OclExpressionCS getEssentialoclcst_oclexpressioncs() {
        return essentialoclcst_oclexpressioncs;
    }

    public void setEssentialoclcst_oclexpressioncs(essentialOCLCST_OclExpressionCS essentialoclcst_oclexpressioncs) {
        this.essentialoclcst_oclexpressioncs = essentialoclcst_oclexpressioncs;
    }
    public List<essentialOCLCST_VariableCS> getEssentialoclcst_variablecss() {
        return essentialoclcst_variablecss;
    }

    public void addEssentialoclcst_variablecs(Essentialoclcst_variablecs essentialoclcst_variablecs) {
        this.essentialoclcst_variablecss.add(essentialoclcst_variablecs);
    }

}