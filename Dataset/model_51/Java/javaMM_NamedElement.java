





import java.util.List;
import java.util.ArrayList;

public class javaMM_NamedElement extends ASTNode {

    private String name;
    private boolean proxy;





    private List<javaMM_ImportDeclaration> javamm_importdeclarations;




    private javaMM_ImportDeclaration javamm_importdeclaration;




    private javaMM_MemberRef javamm_memberref;


    public javaMM_NamedElement(
        String name,        boolean proxy    ) {
        super(
        );
        this.name = name;
        this.proxy = proxy;
        this.javamm_importdeclarations = new ArrayList<>();
    }

    public javaMM_NamedElement(
        String name,        boolean proxy        ArrayList<javaMM_ImportDeclaration> javamm_importdeclarations    ) {
        this.name = name;
        this.proxy = proxy;
        this.javamm_importdeclarations = javamm_importdeclarations;
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

    public List<javaMM_ImportDeclaration> getJavamm_importdeclarations() {
        return javamm_importdeclarations;
    }

    public void addJavamm_importdeclaration(Javamm_importdeclaration javamm_importdeclaration) {
        this.javamm_importdeclarations.add(javamm_importdeclaration);
    }
    public javaMM_ImportDeclaration getJavamm_importdeclaration() {
        return javamm_importdeclaration;
    }

    public void setJavamm_importdeclaration(javaMM_ImportDeclaration javamm_importdeclaration) {
        this.javamm_importdeclaration = javamm_importdeclaration;
    }
    public javaMM_MemberRef getJavamm_memberref() {
        return javamm_memberref;
    }

    public void setJavamm_memberref(javaMM_MemberRef javamm_memberref) {
        this.javamm_memberref = javamm_memberref;
    }

}