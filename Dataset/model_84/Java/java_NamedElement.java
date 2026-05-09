





import java.util.List;
import java.util.ArrayList;

public class java_NamedElement extends ASTNode {

    private String name;
    private boolean proxy;





    private java_ImportDeclaration java_importdeclaration;


    public java_NamedElement(
        String name,        boolean proxy    ) {
        super(
        );
        this.name = name;
        this.proxy = proxy;
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

    public java_ImportDeclaration getJava_importdeclaration() {
        return java_importdeclaration;
    }

    public void setJava_importdeclaration(java_ImportDeclaration java_importdeclaration) {
        this.java_importdeclaration = java_importdeclaration;
    }

}