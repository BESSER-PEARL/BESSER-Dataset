





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_TupleLiteralExpCS extends LiteralExpCS {






    private List<VariableCS> variablecss;


    public ocl_cst_TupleLiteralExpCS(
    ) {
        super(
        );
        this.variablecss = new ArrayList<>();
    }

    public ocl_cst_TupleLiteralExpCS(
        ArrayList<VariableCS> variablecss    ) {
        this.variablecss = variablecss;
    }


    public List<VariableCS> getVariablecss() {
        return variablecss;
    }

    public void addVariablecs(Variablecs variablecs) {
        this.variablecss.add(variablecs);
    }

}