





import java.util.List;
import java.util.ArrayList;

public class mtl_Block extends TemplateExpression {






    private List<OCLExpression> oclexpressions;




    private mtl_LetBlock mtl_letblock;




    private mtl_IfBlock mtl_ifblock;


    public mtl_Block(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public mtl_Block(
        ArrayList<OCLExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public List<OCLExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public mtl_LetBlock getMtl_letblock() {
        return mtl_letblock;
    }

    public void setMtl_letblock(mtl_LetBlock mtl_letblock) {
        this.mtl_letblock = mtl_letblock;
    }
    public mtl_IfBlock getMtl_ifblock() {
        return mtl_ifblock;
    }

    public void setMtl_ifblock(mtl_IfBlock mtl_ifblock) {
        this.mtl_ifblock = mtl_ifblock;
    }

}