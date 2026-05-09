





import java.util.List;
import java.util.ArrayList;

public class JMM_Modifier extends ASTNode {

    private String inheritance;





    private JMM_BodyDeclaration jmm_bodydeclaration;


    public JMM_Modifier(
        String inheritance    ) {
        super(
        );
        this.inheritance = inheritance;
    }


    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }

    public JMM_BodyDeclaration getJmm_bodydeclaration() {
        return jmm_bodydeclaration;
    }

    public void setJmm_bodydeclaration(JMM_BodyDeclaration jmm_bodydeclaration) {
        this.jmm_bodydeclaration = jmm_bodydeclaration;
    }

}