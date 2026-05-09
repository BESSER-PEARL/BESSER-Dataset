





import java.util.List;
import java.util.ArrayList;

public class javaMM_NamedElement extends ASTNode {

    private String proxy;
    private String name;





    private List<javaMM_ImportDeclaration> javamm_importdeclarations;




    private javaMM_ImportDeclaration javamm_importdeclaration;


    public javaMM_NamedElement(
        String proxy,        String name    ) {
        super(
        );
        this.proxy = proxy;
        this.name = name;
        this.javamm_importdeclarations = new ArrayList<>();
    }

    public javaMM_NamedElement(
        String proxy,        String name        ArrayList<javaMM_ImportDeclaration> javamm_importdeclarations    ) {
        this.proxy = proxy;
        this.name = name;
        this.javamm_importdeclarations = javamm_importdeclarations;
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

}