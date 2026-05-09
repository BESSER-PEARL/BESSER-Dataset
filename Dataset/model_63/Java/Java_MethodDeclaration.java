





import java.util.List;
import java.util.ArrayList;

public class Java_MethodDeclaration extends AbstractMethodDeclaration {

    private int extraArrayDimensions;





    private Java_MethodDeclaration java_methoddeclaration;




    private Java_TypeAccess java_typeaccess;




    private List<Java_MethodDeclaration> java_methoddeclarations;


    public Java_MethodDeclaration(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.java_methoddeclarations = new ArrayList<>();
    }

    public Java_MethodDeclaration(
        int extraArrayDimensions        ArrayList<Java_MethodDeclaration> java_methoddeclarations    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.java_methoddeclarations = java_methoddeclarations;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public Java_MethodDeclaration getJava_methoddeclaration() {
        return java_methoddeclaration;
    }

    public void setJava_methoddeclaration(Java_MethodDeclaration java_methoddeclaration) {
        this.java_methoddeclaration = java_methoddeclaration;
    }
    public Java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(Java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }
    public List<Java_MethodDeclaration> getJava_methoddeclarations() {
        return java_methoddeclarations;
    }

    public void addJava_methoddeclaration(Java_methoddeclaration java_methoddeclaration) {
        this.java_methoddeclarations.add(java_methoddeclaration);
    }

}