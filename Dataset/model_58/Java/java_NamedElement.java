





import java.util.List;
import java.util.ArrayList;

public class java_NamedElement extends ASTNode {

    private String name;
    private boolean proxy;





    private java_MemberRef java_memberref;


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

    public java_MemberRef getJava_memberref() {
        return java_memberref;
    }

    public void setJava_memberref(java_MemberRef java_memberref) {
        this.java_memberref = java_memberref;
    }

}