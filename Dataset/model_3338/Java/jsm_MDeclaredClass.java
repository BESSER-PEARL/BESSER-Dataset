





import java.util.List;
import java.util.ArrayList;

public class jsm_MDeclaredClass extends AbstractMDeclaredType, AbstractMClass {






    private jsm_MConstructor jsm_mconstructor;




    private jsm_MInstanceClassFieldDeclaration jsm_minstanceclassfielddeclaration;




    private List<jsm_MInstanceClassFieldDeclaration> jsm_minstanceclassfielddeclarations;




    private jsm_MStaticClassFieldDeclaration jsm_mstaticclassfielddeclaration;




    private jsm_AbstractMClass jsm_abstractmclass;




    private jsm_AbstractMMethodImplementation jsm_abstractmmethodimplementation;




    private List<jsm_AbstractMMethodImplementation> jsm_abstractmmethodimplementations;




    private jsm_MNativeMethodDeclaration jsm_mnativemethoddeclaration;




    private List<jsm_MNativeMethodDeclaration> jsm_mnativemethoddeclarations;




    private List<jsm_MConstructor> jsm_mconstructors;




    private List<jsm_AbstractMInterface> jsm_abstractminterfaces;




    private List<jsm_MStaticClassFieldDeclaration> jsm_mstaticclassfielddeclarations;


    public jsm_MDeclaredClass(
    ) {
        super(
        );
        this.jsm_minstanceclassfielddeclarations = new ArrayList<>();
        this.jsm_abstractmmethodimplementations = new ArrayList<>();
        this.jsm_mnativemethoddeclarations = new ArrayList<>();
        this.jsm_mconstructors = new ArrayList<>();
        this.jsm_abstractminterfaces = new ArrayList<>();
        this.jsm_mstaticclassfielddeclarations = new ArrayList<>();
    }

    public jsm_MDeclaredClass(
        ArrayList<jsm_MInstanceClassFieldDeclaration> jsm_minstanceclassfielddeclarations,        ArrayList<jsm_AbstractMMethodImplementation> jsm_abstractmmethodimplementations,        ArrayList<jsm_MNativeMethodDeclaration> jsm_mnativemethoddeclarations,        ArrayList<jsm_MConstructor> jsm_mconstructors,        ArrayList<jsm_AbstractMInterface> jsm_abstractminterfaces,        ArrayList<jsm_MStaticClassFieldDeclaration> jsm_mstaticclassfielddeclarations    ) {
        this.jsm_minstanceclassfielddeclarations = jsm_minstanceclassfielddeclarations;
        this.jsm_abstractmmethodimplementations = jsm_abstractmmethodimplementations;
        this.jsm_mnativemethoddeclarations = jsm_mnativemethoddeclarations;
        this.jsm_mconstructors = jsm_mconstructors;
        this.jsm_abstractminterfaces = jsm_abstractminterfaces;
        this.jsm_mstaticclassfielddeclarations = jsm_mstaticclassfielddeclarations;
    }


    public jsm_MConstructor getJsm_mconstructor() {
        return jsm_mconstructor;
    }

    public void setJsm_mconstructor(jsm_MConstructor jsm_mconstructor) {
        this.jsm_mconstructor = jsm_mconstructor;
    }
    public jsm_MInstanceClassFieldDeclaration getJsm_minstanceclassfielddeclaration() {
        return jsm_minstanceclassfielddeclaration;
    }

    public void setJsm_minstanceclassfielddeclaration(jsm_MInstanceClassFieldDeclaration jsm_minstanceclassfielddeclaration) {
        this.jsm_minstanceclassfielddeclaration = jsm_minstanceclassfielddeclaration;
    }
    public List<jsm_MInstanceClassFieldDeclaration> getJsm_minstanceclassfielddeclarations() {
        return jsm_minstanceclassfielddeclarations;
    }

    public void addJsm_minstanceclassfielddeclaration(Jsm_minstanceclassfielddeclaration jsm_minstanceclassfielddeclaration) {
        this.jsm_minstanceclassfielddeclarations.add(jsm_minstanceclassfielddeclaration);
    }
    public jsm_MStaticClassFieldDeclaration getJsm_mstaticclassfielddeclaration() {
        return jsm_mstaticclassfielddeclaration;
    }

    public void setJsm_mstaticclassfielddeclaration(jsm_MStaticClassFieldDeclaration jsm_mstaticclassfielddeclaration) {
        this.jsm_mstaticclassfielddeclaration = jsm_mstaticclassfielddeclaration;
    }
    public jsm_AbstractMClass getJsm_abstractmclass() {
        return jsm_abstractmclass;
    }

    public void setJsm_abstractmclass(jsm_AbstractMClass jsm_abstractmclass) {
        this.jsm_abstractmclass = jsm_abstractmclass;
    }
    public jsm_AbstractMMethodImplementation getJsm_abstractmmethodimplementation() {
        return jsm_abstractmmethodimplementation;
    }

    public void setJsm_abstractmmethodimplementation(jsm_AbstractMMethodImplementation jsm_abstractmmethodimplementation) {
        this.jsm_abstractmmethodimplementation = jsm_abstractmmethodimplementation;
    }
    public List<jsm_AbstractMMethodImplementation> getJsm_abstractmmethodimplementations() {
        return jsm_abstractmmethodimplementations;
    }

    public void addJsm_abstractmmethodimplementation(Jsm_abstractmmethodimplementation jsm_abstractmmethodimplementation) {
        this.jsm_abstractmmethodimplementations.add(jsm_abstractmmethodimplementation);
    }
    public jsm_MNativeMethodDeclaration getJsm_mnativemethoddeclaration() {
        return jsm_mnativemethoddeclaration;
    }

    public void setJsm_mnativemethoddeclaration(jsm_MNativeMethodDeclaration jsm_mnativemethoddeclaration) {
        this.jsm_mnativemethoddeclaration = jsm_mnativemethoddeclaration;
    }
    public List<jsm_MNativeMethodDeclaration> getJsm_mnativemethoddeclarations() {
        return jsm_mnativemethoddeclarations;
    }

    public void addJsm_mnativemethoddeclaration(Jsm_mnativemethoddeclaration jsm_mnativemethoddeclaration) {
        this.jsm_mnativemethoddeclarations.add(jsm_mnativemethoddeclaration);
    }
    public List<jsm_MConstructor> getJsm_mconstructors() {
        return jsm_mconstructors;
    }

    public void addJsm_mconstructor(Jsm_mconstructor jsm_mconstructor) {
        this.jsm_mconstructors.add(jsm_mconstructor);
    }
    public List<jsm_AbstractMInterface> getJsm_abstractminterfaces() {
        return jsm_abstractminterfaces;
    }

    public void addJsm_abstractminterface(Jsm_abstractminterface jsm_abstractminterface) {
        this.jsm_abstractminterfaces.add(jsm_abstractminterface);
    }
    public List<jsm_MStaticClassFieldDeclaration> getJsm_mstaticclassfielddeclarations() {
        return jsm_mstaticclassfielddeclarations;
    }

    public void addJsm_mstaticclassfielddeclaration(Jsm_mstaticclassfielddeclaration jsm_mstaticclassfielddeclaration) {
        this.jsm_mstaticclassfielddeclarations.add(jsm_mstaticclassfielddeclaration);
    }

}