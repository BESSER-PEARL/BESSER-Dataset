





import java.util.List;
import java.util.ArrayList;

public class javaMM_BodyDeclaration extends NamedElement {






    private javaMM_Modifier javamm_modifier;




    private javaMM_Modifier javamm_modifier;




    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;




    private javaMM_AnonymousClassDeclaration javamm_anonymousclassdeclaration;




    private List<javaMM_Annotation> javamm_annotations;




    private javaMM_AnonymousClassDeclaration javamm_anonymousclassdeclaration;




    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;


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


    public javaMM_Modifier getJavamm_modifier() {
        return javamm_modifier;
    }

    public void setJavamm_modifier(javaMM_Modifier javamm_modifier) {
        this.javamm_modifier = javamm_modifier;
    }
    public javaMM_Modifier getJavamm_modifier() {
        return javamm_modifier;
    }

    public void setJavamm_modifier(javaMM_Modifier javamm_modifier) {
        this.javamm_modifier = javamm_modifier;
    }
    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }
    public javaMM_AnonymousClassDeclaration getJavamm_anonymousclassdeclaration() {
        return javamm_anonymousclassdeclaration;
    }

    public void setJavamm_anonymousclassdeclaration(javaMM_AnonymousClassDeclaration javamm_anonymousclassdeclaration) {
        this.javamm_anonymousclassdeclaration = javamm_anonymousclassdeclaration;
    }
    public List<javaMM_Annotation> getJavamm_annotations() {
        return javamm_annotations;
    }

    public void addJavamm_annotation(Javamm_annotation javamm_annotation) {
        this.javamm_annotations.add(javamm_annotation);
    }
    public javaMM_AnonymousClassDeclaration getJavamm_anonymousclassdeclaration() {
        return javamm_anonymousclassdeclaration;
    }

    public void setJavamm_anonymousclassdeclaration(javaMM_AnonymousClassDeclaration javamm_anonymousclassdeclaration) {
        this.javamm_anonymousclassdeclaration = javamm_anonymousclassdeclaration;
    }
    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }

}