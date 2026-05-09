





import java.util.List;
import java.util.ArrayList;

public class javaMM_BodyDeclaration extends NamedElement {






    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;




    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;




    private List<javaMM_Annotation> javamm_annotations;


    public javaMM_BodyDeclaration(
    ) {
        super(
        );
        this.javamm_annotations = new ArrayList<>();
    }

    public javaMM_BodyDeclaration(
        ArrayList<javaMM_Annotation> javamm_annotations    ) {
        this.javamm_annotations = javamm_annotations;
    }


    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }
    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }
    public List<javaMM_Annotation> getJavamm_annotations() {
        return javamm_annotations;
    }

    public void addJavamm_annotation(Javamm_annotation javamm_annotation) {
        this.javamm_annotations.add(javamm_annotation);
    }

}