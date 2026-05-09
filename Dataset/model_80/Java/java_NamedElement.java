





import java.util.List;
import java.util.ArrayList;

public class java_NamedElement extends ASTNode {

    private String name;
    private boolean proxy;





    private java_MemberRef java_memberref;




    private List<java_ImportDeclaration> java_importdeclarations;




    private java_ImportDeclaration java_importdeclaration;


    public java_NamedElement(
        String name,        boolean proxy    ) {
        super(
        );
        this.name = name;
        this.proxy = proxy;
        this.java_importdeclarations = new ArrayList<>();
    }

    public java_NamedElement(
        String name,        boolean proxy        ArrayList<java_ImportDeclaration> java_importdeclarations    ) {
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

    public java_MemberRef getJava_memberref() {
        return java_memberref;
    }

    public void setJava_memberref(java_MemberRef java_memberref) {
        this.java_memberref = java_memberref;
    }
    public List<java_ImportDeclaration> getJava_importdeclarations() {
        return java_importdeclarations;
    }

    public void addJava_importdeclaration(Java_importdeclaration java_importdeclaration) {
        this.java_importdeclarations.add(java_importdeclaration);
    }
    public java_ImportDeclaration getJava_importdeclaration() {
        return java_importdeclaration;
    }

    public void setJava_importdeclaration(java_ImportDeclaration java_importdeclaration) {
        this.java_importdeclaration = java_importdeclaration;
    }

}