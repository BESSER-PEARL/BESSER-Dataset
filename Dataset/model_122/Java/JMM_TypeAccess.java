





import java.util.List;
import java.util.ArrayList;

public class JMM_TypeAccess extends Expression, NamespaceAccess {






    private JMM_AbstractTypeDeclaration jmm_abstracttypedeclaration;


    public JMM_TypeAccess(
    ) {
        super(
        );
    }



    public JMM_AbstractTypeDeclaration getJmm_abstracttypedeclaration() {
        return jmm_abstracttypedeclaration;
    }

    public void setJmm_abstracttypedeclaration(JMM_AbstractTypeDeclaration jmm_abstracttypedeclaration) {
        this.jmm_abstracttypedeclaration = jmm_abstracttypedeclaration;
    }

}