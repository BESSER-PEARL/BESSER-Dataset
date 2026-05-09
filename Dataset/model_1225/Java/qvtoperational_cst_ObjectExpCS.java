





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_ObjectExpCS extends cst_ElementWithBody, cst_InstantiationExpCS {

    private boolean isImplicit;





    private List<OCLExpressionCS> oclexpressioncss;




    private SimpleNameCS simplenamecs;


    public qvtoperational_cst_ObjectExpCS(
        boolean isImplicit    ) {
        super(
        );
        this.isImplicit = isImplicit;
        this.oclexpressioncss = new ArrayList<>();
    }

    public qvtoperational_cst_ObjectExpCS(
        boolean isImplicit        ArrayList<OCLExpressionCS> oclexpressioncss    ) {
        this.isImplicit = isImplicit;
        this.oclexpressioncss = oclexpressioncss;
    }

    public boolean getIsimplicit() {
        return isImplicit;
    }

    public void setIsimplicit(boolean isImplicit) {
        this.isImplicit = isImplicit;
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

}