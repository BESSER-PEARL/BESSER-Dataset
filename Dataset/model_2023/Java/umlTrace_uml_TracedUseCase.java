





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedUseCase extends TracedBehavioredClassifier {






    private List<uml_TracedExtend> uml_tracedextends;




    private List<uml_TracedClassifier> uml_tracedclassifiers;




    private List<uml_TracedInclude> uml_tracedincludes;




    private List<uml_TracedExtensionPoint> uml_tracedextensionpoints;


    public umlTrace_uml_TracedUseCase(
    ) {
        super(
        );
        this.uml_tracedextends = new ArrayList<>();
        this.uml_tracedclassifiers = new ArrayList<>();
        this.uml_tracedincludes = new ArrayList<>();
        this.uml_tracedextensionpoints = new ArrayList<>();
    }

    public umlTrace_uml_TracedUseCase(
        ArrayList<uml_TracedExtend> uml_tracedextends,        ArrayList<uml_TracedClassifier> uml_tracedclassifiers,        ArrayList<uml_TracedInclude> uml_tracedincludes,        ArrayList<uml_TracedExtensionPoint> uml_tracedextensionpoints    ) {
        this.uml_tracedextends = uml_tracedextends;
        this.uml_tracedclassifiers = uml_tracedclassifiers;
        this.uml_tracedincludes = uml_tracedincludes;
        this.uml_tracedextensionpoints = uml_tracedextensionpoints;
    }


    public List<uml_TracedExtend> getUml_tracedextends() {
        return uml_tracedextends;
    }

    public void addUml_tracedextend(Uml_tracedextend uml_tracedextend) {
        this.uml_tracedextends.add(uml_tracedextend);
    }
    public List<uml_TracedClassifier> getUml_tracedclassifiers() {
        return uml_tracedclassifiers;
    }

    public void addUml_tracedclassifier(Uml_tracedclassifier uml_tracedclassifier) {
        this.uml_tracedclassifiers.add(uml_tracedclassifier);
    }
    public List<uml_TracedInclude> getUml_tracedincludes() {
        return uml_tracedincludes;
    }

    public void addUml_tracedinclude(Uml_tracedinclude uml_tracedinclude) {
        this.uml_tracedincludes.add(uml_tracedinclude);
    }
    public List<uml_TracedExtensionPoint> getUml_tracedextensionpoints() {
        return uml_tracedextensionpoints;
    }

    public void addUml_tracedextensionpoint(Uml_tracedextensionpoint uml_tracedextensionpoint) {
        this.uml_tracedextensionpoints.add(uml_tracedextensionpoint);
    }

}