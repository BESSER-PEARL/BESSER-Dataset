





import java.util.List;
import java.util.ArrayList;

public class java__BodyDeclaration extends NamedElement {






    private java__AbstractTypeDeclaration java__abstracttypedeclaration;




    private java__AnonymousClassDeclaration java__anonymousclassdeclaration;




    private java__Modifier java__modifier;




    private java__AnonymousClassDeclaration java__anonymousclassdeclaration;




    private java__AbstractTypeDeclaration java__abstracttypedeclaration;




    private java__Modifier java__modifier;




    private List<java__Annotation> java__annotations;


    public java__BodyDeclaration(
    ) {
        super(
        );
        this.java__annotations = new ArrayList<>();
    }

    public java__BodyDeclaration(
        ArrayList<java__Annotation> java__annotations    ) {
        this.java__annotations = java__annotations;
    }


    public java__AbstractTypeDeclaration getJava__abstracttypedeclaration() {
        return java__abstracttypedeclaration;
    }

    public void setJava__abstracttypedeclaration(java__AbstractTypeDeclaration java__abstracttypedeclaration) {
        this.java__abstracttypedeclaration = java__abstracttypedeclaration;
    }
    public java__AnonymousClassDeclaration getJava__anonymousclassdeclaration() {
        return java__anonymousclassdeclaration;
    }

    public void setJava__anonymousclassdeclaration(java__AnonymousClassDeclaration java__anonymousclassdeclaration) {
        this.java__anonymousclassdeclaration = java__anonymousclassdeclaration;
    }
    public java__Modifier getJava__modifier() {
        return java__modifier;
    }

    public void setJava__modifier(java__Modifier java__modifier) {
        this.java__modifier = java__modifier;
    }
    public java__AnonymousClassDeclaration getJava__anonymousclassdeclaration() {
        return java__anonymousclassdeclaration;
    }

    public void setJava__anonymousclassdeclaration(java__AnonymousClassDeclaration java__anonymousclassdeclaration) {
        this.java__anonymousclassdeclaration = java__anonymousclassdeclaration;
    }
    public java__AbstractTypeDeclaration getJava__abstracttypedeclaration() {
        return java__abstracttypedeclaration;
    }

    public void setJava__abstracttypedeclaration(java__AbstractTypeDeclaration java__abstracttypedeclaration) {
        this.java__abstracttypedeclaration = java__abstracttypedeclaration;
    }
    public java__Modifier getJava__modifier() {
        return java__modifier;
    }

    public void setJava__modifier(java__Modifier java__modifier) {
        this.java__modifier = java__modifier;
    }
    public List<java__Annotation> getJava__annotations() {
        return java__annotations;
    }

    public void addJava__annotation(Java__annotation java__annotation) {
        this.java__annotations.add(java__annotation);
    }

}