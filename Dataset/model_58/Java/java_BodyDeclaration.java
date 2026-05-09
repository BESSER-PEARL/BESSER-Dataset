





import java.util.List;
import java.util.ArrayList;

public class java_BodyDeclaration extends NamedElement {






    private java_AbstractTypeDeclaration java_abstracttypedeclaration;




    private java_AnonymousClassDeclaration java_anonymousclassdeclaration;




    private java_AnonymousClassDeclaration java_anonymousclassdeclaration;




    private java_Modifier java_modifier;




    private java_Modifier java_modifier;




    private java_AbstractTypeDeclaration java_abstracttypedeclaration;




    private List<java_Annotation> java_annotations;


    public java_BodyDeclaration(
    ) {
        super(
        );
        this.java_annotations = new ArrayList<>();
    }

    public java_BodyDeclaration(
        ArrayList<java_Annotation> java_annotations    ) {
        this.java_annotations = java_annotations;
    }


    public java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }
    public java_AnonymousClassDeclaration getJava_anonymousclassdeclaration() {
        return java_anonymousclassdeclaration;
    }

    public void setJava_anonymousclassdeclaration(java_AnonymousClassDeclaration java_anonymousclassdeclaration) {
        this.java_anonymousclassdeclaration = java_anonymousclassdeclaration;
    }
    public java_AnonymousClassDeclaration getJava_anonymousclassdeclaration() {
        return java_anonymousclassdeclaration;
    }

    public void setJava_anonymousclassdeclaration(java_AnonymousClassDeclaration java_anonymousclassdeclaration) {
        this.java_anonymousclassdeclaration = java_anonymousclassdeclaration;
    }
    public java_Modifier getJava_modifier() {
        return java_modifier;
    }

    public void setJava_modifier(java_Modifier java_modifier) {
        this.java_modifier = java_modifier;
    }
    public java_Modifier getJava_modifier() {
        return java_modifier;
    }

    public void setJava_modifier(java_Modifier java_modifier) {
        this.java_modifier = java_modifier;
    }
    public java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }
    public List<java_Annotation> getJava_annotations() {
        return java_annotations;
    }

    public void addJava_annotation(Java_annotation java_annotation) {
        this.java_annotations.add(java_annotation);
    }

}