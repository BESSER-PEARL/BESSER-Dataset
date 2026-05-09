





import java.util.List;
import java.util.ArrayList;

public class java_NamedElement extends ASTNode {

    private boolean proxy;
    private String name;





    private List<java_ImportDeclaration> java_importdeclarations;




    private java_ImportDeclaration java_importdeclaration;




    private java_MemberRef java_memberref;


    public java_NamedElement(
        boolean proxy,        String name    ) {
        super(
        );
        this.proxy = proxy;
        this.name = name;
        this.java_importdeclarations = new ArrayList<>();
    }

    public java_NamedElement(
        boolean proxy,        String name        ArrayList<java_ImportDeclaration> java_importdeclarations    ) {
        this.proxy = proxy;
        this.name = name;
        this.java_importdeclarations = java_importdeclarations;
    }

    public boolean getProxy() {
        return proxy;
    }

    public void setProxy(boolean proxy) {
        this.proxy = proxy;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public java_MemberRef getJava_memberref() {
        return java_memberref;
    }

    public void setJava_memberref(java_MemberRef java_memberref) {
        this.java_memberref = java_memberref;
    }

}