





import java.util.List;
import java.util.ArrayList;

public class essentialOCLCST_TupleLiteralExpCS extends LiteralExpCS {






    private List<essentialOCLCST_VariableCS> essentialoclcst_variablecss;


    public essentialOCLCST_TupleLiteralExpCS(
    ) {
        super(
        );
        this.essentialoclcst_variablecss = new ArrayList<>();
    }

    public essentialOCLCST_TupleLiteralExpCS(
        ArrayList<essentialOCLCST_VariableCS> essentialoclcst_variablecss    ) {
        this.essentialoclcst_variablecss = essentialoclcst_variablecss;
    }


    public List<essentialOCLCST_VariableCS> getEssentialoclcst_variablecss() {
        return essentialoclcst_variablecss;
    }

    public void addEssentialoclcst_variablecs(Essentialoclcst_variablecs essentialoclcst_variablecs) {
        this.essentialoclcst_variablecss.add(essentialoclcst_variablecs);
    }

}