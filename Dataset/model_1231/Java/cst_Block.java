





import java.util.List;
import java.util.ArrayList;

public class cst_Block extends TemplateExpression {






    private cst_InitSection cst_initsection;




    private List<cst_TemplateExpression> cst_templateexpressions;


    public cst_Block(
    ) {
        super(
        );
        this.cst_templateexpressions = new ArrayList<>();
    }

    public cst_Block(
        ArrayList<cst_TemplateExpression> cst_templateexpressions    ) {
        this.cst_templateexpressions = cst_templateexpressions;
    }


    public cst_InitSection getCst_initsection() {
        return cst_initsection;
    }

    public void setCst_initsection(cst_InitSection cst_initsection) {
        this.cst_initsection = cst_initsection;
    }
    public List<cst_TemplateExpression> getCst_templateexpressions() {
        return cst_templateexpressions;
    }

    public void addCst_templateexpression(Cst_templateexpression cst_templateexpression) {
        this.cst_templateexpressions.add(cst_templateexpression);
    }

}