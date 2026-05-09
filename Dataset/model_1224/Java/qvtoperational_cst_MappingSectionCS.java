





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_MappingSectionCS extends cst_CSTNode, cst_ElementWithBody {






    private List<OCLExpressionCS> oclexpressioncss;


    public qvtoperational_cst_MappingSectionCS(
    ) {
        super(
        );
        this.oclexpressioncss = new ArrayList<>();
    }

    public qvtoperational_cst_MappingSectionCS(
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