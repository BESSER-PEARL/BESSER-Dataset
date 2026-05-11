





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedClass extends uml_TracedBehavioredClassifier, uml_TracedEncapsulatedClassifier {






    private List<uml_TracedExtension> uml_tracedextensions;




    private List<uml_TracedOperation> uml_tracedoperations;




    private List<uml_TracedClass> uml_tracedclasss;




    private List<uml_TracedReception> uml_tracedreceptions;


    public umlTrace_uml_TracedClass(
    ) {
        super(
        );
        this.uml_tracedextensions = new ArrayList<>();
        this.uml_tracedoperations = new ArrayList<>();
        this.uml_tracedclasss = new ArrayList<>();
        this.uml_tracedreceptions = new ArrayList<>();
    }

    public umlTrace_uml_TracedClass(
        ArrayList<uml_TracedExtension> uml_tracedextensions,        ArrayList<uml_TracedOperation> uml_tracedoperations,        ArrayList<uml_TracedClass> uml_tracedclasss,        ArrayList<uml_TracedReception> uml_tracedreceptions    ) {
        this.uml_tracedextensions = uml_tracedextensions;
        this.uml_tracedoperations = uml_tracedoperations;
        this.uml_tracedclasss = uml_tracedclasss;
        this.uml_tracedreceptions = uml_tracedreceptions;
    }


    public List<uml_TracedExtension> getUml_tracedextensions() {
        return uml_tracedextensions;
    }

    public void addUml_tracedextension(Uml_tracedextension uml_tracedextension) {
        this.uml_tracedextensions.add(uml_tracedextension);
    }
    public List<uml_TracedOperation> getUml_tracedoperations() {
        return uml_tracedoperations;
    }

    public void addUml_tracedoperation(Uml_tracedoperation uml_tracedoperation) {
        this.uml_tracedoperations.add(uml_tracedoperation);
    }
    public List<uml_TracedClass> getUml_tracedclasss() {
        return uml_tracedclasss;
    }

    public void addUml_tracedclass(Uml_tracedclass uml_tracedclass) {
        this.uml_tracedclasss.add(uml_tracedclass);
    }
    public List<uml_TracedReception> getUml_tracedreceptions() {
        return uml_tracedreceptions;
    }

    public void addUml_tracedreception(Uml_tracedreception uml_tracedreception) {
        this.uml_tracedreceptions.add(uml_tracedreception);
    }

}