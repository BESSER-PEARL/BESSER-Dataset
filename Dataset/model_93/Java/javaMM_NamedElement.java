





import java.util.List;
import java.util.ArrayList;

public class javaMM_NamedElement extends ASTNode {

    private String proxy;
    private String name;





    private javaMM_MemberRef javamm_memberref;


    public javaMM_NamedElement(
        String proxy,        String name    ) {
        super(
        );
        this.proxy = proxy;
        this.name = name;
    }


    public String getProxy() {
        return proxy;
    }

    public void setProxy(String proxy) {
        this.proxy = proxy;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public javaMM_MemberRef getJavamm_memberref() {
        return javamm_memberref;
    }

    public void setJavamm_memberref(javaMM_MemberRef javamm_memberref) {
        this.javamm_memberref = javamm_memberref;
    }

}