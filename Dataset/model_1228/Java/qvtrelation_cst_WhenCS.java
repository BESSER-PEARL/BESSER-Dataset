





import java.util.List;
import java.util.ArrayList;

public class qvtrelation_cst_WhenCS extends CSTNode {






    private List<OCLExpressionCS> oclexpressioncss;


    public qvtrelation_cst_WhenCS(
    ) {
        super(
        );
        this.oclexpressioncss = new ArrayList<>();
    }

    public qvtrelation_cst_WhenCS(
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