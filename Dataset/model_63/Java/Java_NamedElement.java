





import java.util.List;
import java.util.ArrayList;

public class Java_NamedElement extends ASTNode {

    private String name;
    private boolean proxy;





    private Java_ImportDeclaration java_importdeclaration;




    private Java_MemberRef java_memberref;




    private List<Java_ImportDeclaration> java_importdeclarations;


    public Java_NamedElement(
        String name,        boolean proxy    ) {
        super(
        );
        this.name = name;
        this.proxy = proxy;
        this.java_importdeclarations = new ArrayList<>();
    }

    public Java_NamedElement(
        String name,        boolean proxy        ArrayList<Java_ImportDeclaration> java_importdeclarations    ) {
        this.name = name;
        this.proxy = proxy;
        this.java_importdeclarations = java_importdeclarations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getProxy() {
        return proxy;
    }

    public void setProxy(boolean proxy) {
        this.proxy = proxy;
    }

    public Java_ImportDeclaration getJava_importdeclaration() {
        return java_importdeclaration;
    }

    public void setJava_importdeclaration(Java_ImportDeclaration java_importdeclaration) {
        this.java_importdeclaration = java_importdeclaration;
    }
    public Java_MemberRef getJava_memberref() {
        return java_memberref;
    }

    public void setJava_memberref(Java_MemberRef java_memberref) {
        this.java_memberref = java_memberref;
    }
    public List<Java_ImportDeclaration> getJava_importdeclarations() {
        return java_importdeclarations;
    }

    public void addJava_importdeclaration(Java_importdeclaration java_importdeclaration) {
        this.java_importdeclarations.add(java_importdeclaration);
    }

}