





import java.util.List;
import java.util.ArrayList;

public class VariableDecl  {






    private ACG_LetExp acg_letexp;




    private ACG_IteratorExp acg_iteratorexp;




    private ACG_VariableExp acg_variableexp;


    public VariableDecl(
    ) {
    }



    public ACG_LetExp getAcg_letexp() {
        return acg_letexp;
    }

    public void setAcg_letexp(ACG_LetExp acg_letexp) {
        this.acg_letexp = acg_letexp;
    }
    public ACG_IteratorExp getAcg_iteratorexp() {
        return acg_iteratorexp;
    }

    public void setAcg_iteratorexp(ACG_IteratorExp acg_iteratorexp) {
        this.acg_iteratorexp = acg_iteratorexp;
    }
    public ACG_VariableExp getAcg_variableexp() {
        return acg_variableexp;
    }

    public void setAcg_variableexp(ACG_VariableExp acg_variableexp) {
        this.acg_variableexp = acg_variableexp;
    }

}