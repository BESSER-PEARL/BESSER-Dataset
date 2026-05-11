





import java.util.List;
import java.util.ArrayList;

public class alf_LocalNameDeclarationOrExpressionStatement extends Statement {






    private alf_Name alf_name;




    private alf_NameToExpressionCompletion alf_nametoexpressioncompletion;




    private alf_MultiplicityIndicator alf_multiplicityindicator;




    private alf_NonNameExpression alf_nonnameexpression;




    private alf_QualifiedName alf_qualifiedname;


    public alf_LocalNameDeclarationOrExpressionStatement(
    ) {
        super(
        );
    }



    public alf_Name getAlf_name() {
        return alf_name;
    }

    public void setAlf_name(alf_Name alf_name) {
        this.alf_name = alf_name;
    }
    public alf_NameToExpressionCompletion getAlf_nametoexpressioncompletion() {
        return alf_nametoexpressioncompletion;
    }

    public void setAlf_nametoexpressioncompletion(alf_NameToExpressionCompletion alf_nametoexpressioncompletion) {
        this.alf_nametoexpressioncompletion = alf_nametoexpressioncompletion;
    }
    public alf_MultiplicityIndicator getAlf_multiplicityindicator() {
        return alf_multiplicityindicator;
    }

    public void setAlf_multiplicityindicator(alf_MultiplicityIndicator alf_multiplicityindicator) {
        this.alf_multiplicityindicator = alf_multiplicityindicator;
    }
    public alf_NonNameExpression getAlf_nonnameexpression() {
        return alf_nonnameexpression;
    }

    public void setAlf_nonnameexpression(alf_NonNameExpression alf_nonnameexpression) {
        this.alf_nonnameexpression = alf_nonnameexpression;
    }
    public alf_QualifiedName getAlf_qualifiedname() {
        return alf_qualifiedname;
    }

    public void setAlf_qualifiedname(alf_QualifiedName alf_qualifiedname) {
        this.alf_qualifiedname = alf_qualifiedname;
    }

}