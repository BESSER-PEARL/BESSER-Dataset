





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_BlockExpCS extends StatementCS {






    private List<OCLExpressionCS> oclexpressioncss;


    public qvtoperational_cst_BlockExpCS(
    ) {
        super(
        );
        this.oclexpressioncss = new ArrayList<>();
    }

    public qvtoperational_cst_BlockExpCS(
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