





import java.util.List;
import java.util.ArrayList;

public class java__NamedElement extends ASTNode {

    private String name;
    private boolean proxy;





    private java__ImportDeclaration java__importdeclaration;




    private List<java__ImportDeclaration> java__importdeclarations;


    public java__NamedElement(
        String name,        boolean proxy    ) {
        super(
        );
        this.name = name;
        this.proxy = proxy;
        this.java__importdeclarations = new ArrayList<>();
    }

    public java__NamedElement(
        String name,        boolean proxy        ArrayList<java__ImportDeclaration> java__importdeclarations    ) {
        this.name = name;
        this.proxy = proxy;
        this.java__importdeclarations = java__importdeclarations;
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

    public java__ImportDeclaration getJava__importdeclaration() {
        return java__importdeclaration;
    }

    public void setJava__importdeclaration(java__ImportDeclaration java__importdeclaration) {
        this.java__importdeclaration = java__importdeclaration;
    }
    public List<java__ImportDeclaration> getJava__importdeclarations() {
        return java__importdeclarations;
    }

    public void addJava__importdeclaration(Java__importdeclaration java__importdeclaration) {
        this.java__importdeclarations.add(java__importdeclaration);
    }

}