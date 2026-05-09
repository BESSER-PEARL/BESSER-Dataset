





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_QMM_OCL_OclType extends LocatedElement {

    private String name;





    private OclExpression oclexpression;




    private VariableDeclaration variabledeclaration;


    public QualityMetamodel_QMM_OCL_OclType(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public VariableDeclaration getVariabledeclaration() {
        return variabledeclaration;
    }

    public void setVariabledeclaration(VariableDeclaration variabledeclaration) {
        this.variabledeclaration = variabledeclaration;
    }

}