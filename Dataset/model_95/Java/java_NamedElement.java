





import java.util.List;
import java.util.ArrayList;

public class java_NamedElement extends ASTNode {

    private boolean proxy;
    private String name;





    private java_ImportDeclaration java_importdeclaration;


    public java_NamedElement(
        boolean proxy,        String name    ) {
        super(
        );
        this.proxy = proxy;
        this.name = name;
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

    public java_ImportDeclaration getJava_importdeclaration() {
        return java_importdeclaration;
    }

    public void setJava_importdeclaration(java_ImportDeclaration java_importdeclaration) {
        this.java_importdeclaration = java_importdeclaration;
    }

}