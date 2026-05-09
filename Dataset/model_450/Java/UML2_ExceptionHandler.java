





import java.util.List;
import java.util.ArrayList;

public class UML2_ExceptionHandler extends Element {






    private UML2_ObjectNode uml2_objectnode;




    private UML2_ExecutableNode uml2_executablenode;




    private List<UML2_Classifier> uml2_classifiers;




    private UML2_ExecutableNode uml2_executablenode;




    private UML2_ExecutableNode uml2_executablenode;


    public UML2_ExceptionHandler(
    ) {
        super(
        );
        this.uml2_classifiers = new ArrayList<>();
    }

    public UML2_ExceptionHandler(
        ArrayList<UML2_Classifier> uml2_classifiers    ) {
        this.uml2_classifiers = uml2_classifiers;
    }


    public UML2_ObjectNode getUml2_objectnode() {
        return uml2_objectnode;
    }

    public void setUml2_objectnode(UML2_ObjectNode uml2_objectnode) {
        this.uml2_objectnode = uml2_objectnode;
    }
    public UML2_ExecutableNode getUml2_executablenode() {
        return uml2_executablenode;
    }

    public void setUml2_executablenode(UML2_ExecutableNode uml2_executablenode) {
        this.uml2_executablenode = uml2_executablenode;
    }
    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }
    public UML2_ExecutableNode getUml2_executablenode() {
        return uml2_executablenode;
    }

    public void setUml2_executablenode(UML2_ExecutableNode uml2_executablenode) {
        this.uml2_executablenode = uml2_executablenode;
    }
    public UML2_ExecutableNode getUml2_executablenode() {
        return uml2_executablenode;
    }

    public void setUml2_executablenode(UML2_ExecutableNode uml2_executablenode) {
        this.uml2_executablenode = uml2_executablenode;
    }

}