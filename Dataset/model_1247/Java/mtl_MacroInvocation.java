





import java.util.List;
import java.util.ArrayList;

public class mtl_MacroInvocation extends TemplateExpression {






    private List<OCLExpression> oclexpressions;




    private mtl_Macro mtl_macro;


    public mtl_MacroInvocation(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public mtl_MacroInvocation(
        ArrayList<OCLExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public List<OCLExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public mtl_Macro getMtl_macro() {
        return mtl_macro;
    }

    public void setMtl_macro(mtl_Macro mtl_macro) {
        this.mtl_macro = mtl_macro;
    }

}