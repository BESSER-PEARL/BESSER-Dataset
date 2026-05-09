





import java.util.List;
import java.util.ArrayList;

public class javaless_EClass extends EClassifier {

    private boolean abstract;
    private boolean interface;





    private javaless_EClass javaless_eclass;




    private List<javaless_EClass> javaless_eclasss;


    public javaless_EClass(
        boolean abstract,        boolean interface    ) {
        super(
        );
        this.abstract = abstract;
        this.interface = interface;
        this.javaless_eclasss = new ArrayList<>();
    }

    public javaless_EClass(
        boolean abstract,        boolean interface        ArrayList<javaless_EClass> javaless_eclasss    ) {
        this.abstract = abstract;
        this.interface = interface;
        this.javaless_eclasss = javaless_eclasss;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }

    public javaless_EClass getJavaless_eclass() {
        return javaless_eclass;
    }

    public void setJavaless_eclass(javaless_EClass javaless_eclass) {
        this.javaless_eclass = javaless_eclass;
    }
    public List<javaless_EClass> getJavaless_eclasss() {
        return javaless_eclasss;
    }

    public void addJavaless_eclass(Javaless_eclass javaless_eclass) {
        this.javaless_eclasss.add(javaless_eclass);
    }

}