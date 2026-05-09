





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_ModelTypeCS extends cst_CSTNode, cst_ElementWithBody {






    private List<OCLExpressionCS> oclexpressioncss;




    private SimpleNameCS simplenamecs;




    private StringLiteralExpCS stringliteralexpcs;


    public qvtoperational_cst_ModelTypeCS(
    ) {
        super(
        );
        this.oclexpressioncss = new ArrayList<>();
    }

    public qvtoperational_cst_ModelTypeCS(
        ArrayList<OCLExpressionCS> oclexpressioncss    ) {
        this.oclexpressioncss = oclexpressioncss;
    }


    public List<OCLExpressionCS> getOclexpressioncss() {
        return oclexpressioncss;
    }

    public void addOclexpressioncs(Oclexpressioncs oclexpressioncs) {
        this.oclexpressioncss.add(oclexpressioncs);
    }
    public SimpleNameCS getSimplenamecs() {
        return simplenamecs;
    }

    public void setSimplenamecs(SimpleNameCS simplenamecs) {
        this.simplenamecs = simplenamecs;
    }
    public StringLiteralExpCS getStringliteralexpcs() {
        return stringliteralexpcs;
    }

    public void setStringliteralexpcs(StringLiteralExpCS stringliteralexpcs) {
        this.stringliteralexpcs = stringliteralexpcs;
    }

}