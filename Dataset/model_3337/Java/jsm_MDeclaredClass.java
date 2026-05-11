





import java.util.List;
import java.util.ArrayList;

public class jsm_MDeclaredClass extends AbstractMDeclaredType, AbstractMClass {






    private jsm_AbstractMClass jsm_abstractmclass;




    private List<jsm_AbstractMMethodImplementation> jsm_abstractmmethodimplementations;




    private jsm_AbstractMMethodImplementation jsm_abstractmmethodimplementation;




    private List<jsm_AbstractMInterface> jsm_abstractminterfaces;


    public jsm_MDeclaredClass(
    ) {
        super(
        );
        this.jsm_abstractmmethodimplementations = new ArrayList<>();
        this.jsm_abstractminterfaces = new ArrayList<>();
    }

    public jsm_MDeclaredClass(
        ArrayList<jsm_AbstractMMethodImplementation> jsm_abstractmmethodimplementations,        ArrayList<jsm_AbstractMInterface> jsm_abstractminterfaces    ) {
        this.jsm_abstractmmethodimplementations = jsm_abstractmmethodimplementations;
        this.jsm_abstractminterfaces = jsm_abstractminterfaces;
    }


    public jsm_AbstractMClass getJsm_abstractmclass() {
        return jsm_abstractmclass;
    }

    public void setJsm_abstractmclass(jsm_AbstractMClass jsm_abstractmclass) {
        this.jsm_abstractmclass = jsm_abstractmclass;
    }
    public List<jsm_AbstractMMethodImplementation> getJsm_abstractmmethodimplementations() {
        return jsm_abstractmmethodimplementations;
    }

    public void addJsm_abstractmmethodimplementation(Jsm_abstractmmethodimplementation jsm_abstractmmethodimplementation) {
        this.jsm_abstractmmethodimplementations.add(jsm_abstractmmethodimplementation);
    }
    public jsm_AbstractMMethodImplementation getJsm_abstractmmethodimplementation() {
        return jsm_abstractmmethodimplementation;
    }

    public void setJsm_abstractmmethodimplementation(jsm_AbstractMMethodImplementation jsm_abstractmmethodimplementation) {
        this.jsm_abstractmmethodimplementation = jsm_abstractmmethodimplementation;
    }
    public List<jsm_AbstractMInterface> getJsm_abstractminterfaces() {
        return jsm_abstractminterfaces;
    }

    public void addJsm_abstractminterface(Jsm_abstractminterface jsm_abstractminterface) {
        this.jsm_abstractminterfaces.add(jsm_abstractminterface);
    }

}