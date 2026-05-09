





import java.util.List;
import java.util.ArrayList;

public class graphbt_FormulaList  {






    private List<graphbt_Formula> graphbt_formulas;


    public graphbt_FormulaList(
    ) {
        this.graphbt_formulas = new ArrayList<>();
    }

    public graphbt_FormulaList(
        ArrayList<graphbt_Formula> graphbt_formulas    ) {
        this.graphbt_formulas = graphbt_formulas;
    }


    public List<graphbt_Formula> getGraphbt_formulas() {
        return graphbt_formulas;
    }

    public void addGraphbt_formula(Graphbt_formula graphbt_formula) {
        this.graphbt_formulas.add(graphbt_formula);
    }

}