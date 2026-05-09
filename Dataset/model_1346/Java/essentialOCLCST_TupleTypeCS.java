





import java.util.List;
import java.util.ArrayList;

public class essentialOCLCST_TupleTypeCS extends TypeLiteralExpCS, TypeCS {

    private String value;





    private List<essentialOCLCST_VariableCS> essentialoclcst_variablecss;


    public essentialOCLCST_TupleTypeCS(
        String value    ) {
        super(
        );
        this.value = value;
        this.essentialoclcst_variablecss = new ArrayList<>();
    }

    public essentialOCLCST_TupleTypeCS(
        String value        ArrayList<essentialOCLCST_VariableCS> essentialoclcst_variablecss    ) {
        this.value = value;
        this.essentialoclcst_variablecss = essentialoclcst_variablecss;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<essentialOCLCST_VariableCS> getEssentialoclcst_variablecss() {
        return essentialoclcst_variablecss;
    }

    public void addEssentialoclcst_variablecs(Essentialoclcst_variablecs essentialoclcst_variablecs) {
        this.essentialoclcst_variablecss.add(essentialoclcst_variablecs);
    }

}