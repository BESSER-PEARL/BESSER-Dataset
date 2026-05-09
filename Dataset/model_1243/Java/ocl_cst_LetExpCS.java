





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_LetExpCS extends OCLExpressionCS {






    private List<VariableCS> variablecss;


    public ocl_cst_LetExpCS(
    ) {
        super(
        );
        this.variablecss = new ArrayList<>();
    }

    public ocl_cst_LetExpCS(
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