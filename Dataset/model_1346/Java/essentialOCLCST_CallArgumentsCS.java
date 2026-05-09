





import java.util.List;
import java.util.ArrayList;

public class essentialOCLCST_CallArgumentsCS  {






    private essentialOCLCST_CallExpCS essentialoclcst_callexpcs;




    private List<essentialOCLCST_OclExpressionCS> essentialoclcst_oclexpressioncss;




    private essentialOCLCST_PathNameCS essentialoclcst_pathnamecs;


    public essentialOCLCST_CallArgumentsCS(
    ) {
        this.essentialoclcst_oclexpressioncss = new ArrayList<>();
    }

    public essentialOCLCST_CallArgumentsCS(
        ArrayList<essentialOCLCST_OclExpressionCS> essentialoclcst_oclexpressioncss    ) {
        this.essentialoclcst_oclexpressioncss = essentialoclcst_oclexpressioncss;
    }


    public essentialOCLCST_CallExpCS getEssentialoclcst_callexpcs() {
        return essentialoclcst_callexpcs;
    }

    public void setEssentialoclcst_callexpcs(essentialOCLCST_CallExpCS essentialoclcst_callexpcs) {
        this.essentialoclcst_callexpcs = essentialoclcst_callexpcs;
    }
    public List<essentialOCLCST_OclExpressionCS> getEssentialoclcst_oclexpressioncss() {
        return essentialoclcst_oclexpressioncss;
    }

    public void addEssentialoclcst_oclexpressioncs(Essentialoclcst_oclexpressioncs essentialoclcst_oclexpressioncs) {
        this.essentialoclcst_oclexpressioncss.add(essentialoclcst_oclexpressioncs);
    }
    public essentialOCLCST_PathNameCS getEssentialoclcst_pathnamecs() {
        return essentialoclcst_pathnamecs;
    }

    public void setEssentialoclcst_pathnamecs(essentialOCLCST_PathNameCS essentialoclcst_pathnamecs) {
        this.essentialoclcst_pathnamecs = essentialoclcst_pathnamecs;
    }

}