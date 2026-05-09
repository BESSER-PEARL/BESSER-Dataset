





import java.util.List;
import java.util.ArrayList;

public class java__MethodDeclaration extends AbstractMethodDeclaration {

    private int extraArrayDimensions;





    private java__MethodDeclaration java__methoddeclaration;




    private List<java__MethodDeclaration> java__methoddeclarations;


    public java__MethodDeclaration(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.java__methoddeclarations = new ArrayList<>();
    }

    public java__MethodDeclaration(
        int extraArrayDimensions        ArrayList<java__MethodDeclaration> java__methoddeclarations    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.java__methoddeclarations = java__methoddeclarations;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public java__MethodDeclaration getJava__methoddeclaration() {
        return java__methoddeclaration;
    }

    public void setJava__methoddeclaration(java__MethodDeclaration java__methoddeclaration) {
        this.java__methoddeclaration = java__methoddeclaration;
    }
    public List<java__MethodDeclaration> getJava__methoddeclarations() {
        return java__methoddeclarations;
    }

    public void addJava__methoddeclaration(Java__methoddeclaration java__methoddeclaration) {
        this.java__methoddeclarations.add(java__methoddeclaration);
    }

}