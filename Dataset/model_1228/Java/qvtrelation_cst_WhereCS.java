





import java.util.List;
import java.util.ArrayList;

public class qvtrelation_cst_WhereCS extends CSTNode {






    private List<OCLExpressionCS> oclexpressioncss;


    public qvtrelation_cst_WhereCS(
    ) {
        super(
        );
        this.oclexpressioncss = new ArrayList<>();
    }

    public qvtrelation_cst_WhereCS(
        ArrayList<OCLExpressionCS> oclexpressioncss    ) {
        this.oclexpressioncss = oclexpressioncss;
    }


    public List<OCLExpressionCS> getOclexpressioncss() {
        return oclexpressioncss;
    }

    public void addOclexpressioncs(Oclexpressioncs oclexpressioncs) {
        this.oclexpressioncss.add(oclexpressioncs);
    }

}