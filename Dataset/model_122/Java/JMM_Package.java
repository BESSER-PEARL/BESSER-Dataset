





import java.util.List;
import java.util.ArrayList;

public class JMM_Package extends NamedElement {






    private JMM_Package jmm_package;




    private List<JMM_AbstractTypeDeclaration> jmm_abstracttypedeclarations;




    private JMM_Model jmm_model;


    public JMM_Package(
    ) {
        super(
        );
        this.jmm_abstracttypedeclarations = new ArrayList<>();
    }

    public JMM_Package(
        ArrayList<JMM_AbstractTypeDeclaration> jmm_abstracttypedeclarations    ) {
        this.jmm_abstracttypedeclarations = jmm_abstracttypedeclarations;
    }


    public JMM_Package getJmm_package() {
        return jmm_package;
    }

    public void setJmm_package(JMM_Package jmm_package) {
        this.jmm_package = jmm_package;
    }
    public List<JMM_AbstractTypeDeclaration> getJmm_abstracttypedeclarations() {
        return jmm_abstracttypedeclarations;
    }

    public void addJmm_abstracttypedeclaration(Jmm_abstracttypedeclaration jmm_abstracttypedeclaration) {
        this.jmm_abstracttypedeclarations.add(jmm_abstracttypedeclaration);
    }
    public JMM_Model getJmm_model() {
        return jmm_model;
    }

    public void setJmm_model(JMM_Model jmm_model) {
        this.jmm_model = jmm_model;
    }

}