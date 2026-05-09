





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_InstantiationExpCS extends StatementCS {






    private TypeSpecCS typespeccs;




    private List<OCLExpressionCS> oclexpressioncss;


    public qvtoperational_cst_InstantiationExpCS(
    ) {
        super(
        );
        this.oclexpressioncss = new ArrayList<>();
    }

    public qvtoperational_cst_InstantiationExpCS(
        ArrayList<OCLExpressionCS> oclexpressioncss    ) {
        this.oclexpressioncss = oclexpressioncss;
    }


    public TypeSpecCS getTypespeccs() {
        return typespeccs;
    }

    public void setTypespeccs(TypeSpecCS typespeccs) {
        this.typespeccs = typespeccs;
    }
    public List<OCLExpressionCS> getOclexpressioncss() {
        return oclexpressioncss;
    }

    public void addOclexpressioncs(Oclexpressioncs oclexpressioncs) {
        this.oclexpressioncss.add(oclexpressioncs);
    }

}