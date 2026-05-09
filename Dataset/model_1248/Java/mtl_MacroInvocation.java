





import java.util.List;
import java.util.ArrayList;

public class mtl_MacroInvocation extends TemplateExpression {






    private mtl_Macro mtl_macro;




    private List<OCLExpression> oclexpressions;


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


    public mtl_Macro getMtl_macro() {
        return mtl_macro;
    }

    public void setMtl_macro(mtl_Macro mtl_macro) {
        this.mtl_macro = mtl_macro;
    }
    public List<OCLExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}