





import java.util.List;
import java.util.ArrayList;

public class graphbt_Formula  {

    private String formulaName;





    private graphbt_FormulaList graphbt_formulalist;


    public graphbt_Formula(
        String formulaName    ) {
        this.formulaName = formulaName;
    }


    public String getFormulaname() {
        return formulaName;
    }

    public void setFormulaname(String formulaName) {
        this.formulaName = formulaName;
    }

    public graphbt_FormulaList getGraphbt_formulalist() {
        return graphbt_formulalist;
    }

    public void setGraphbt_formulalist(graphbt_FormulaList graphbt_formulalist) {
        this.graphbt_formulalist = graphbt_formulalist;
    }

}