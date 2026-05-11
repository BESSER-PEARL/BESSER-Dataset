





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedInterface extends TracedClassifier {






    private List<uml_TracedOperation> uml_tracedoperations;




    private List<uml_TracedInterface> uml_tracedinterfaces;




    private uml_TracedProtocolStateMachine uml_tracedprotocolstatemachine;




    private List<uml_TracedReception> uml_tracedreceptions;




    private List<uml_TracedProperty> uml_tracedpropertys;




    private List<uml_TracedClassifier> uml_tracedclassifiers;


    public umlTrace_uml_TracedInterface(
    ) {
        super(
        );
        this.uml_tracedoperations = new ArrayList<>();
        this.uml_tracedinterfaces = new ArrayList<>();
        this.uml_tracedreceptions = new ArrayList<>();
        this.uml_tracedpropertys = new ArrayList<>();
        this.uml_tracedclassifiers = new ArrayList<>();
    }

    public umlTrace_uml_TracedInterface(
        ArrayList<uml_TracedOperation> uml_tracedoperations,        ArrayList<uml_TracedInterface> uml_tracedinterfaces,        ArrayList<uml_TracedReception> uml_tracedreceptions,        ArrayList<uml_TracedProperty> uml_tracedpropertys,        ArrayList<uml_TracedClassifier> uml_tracedclassifiers    ) {
        this.uml_tracedoperations = uml_tracedoperations;
        this.uml_tracedinterfaces = uml_tracedinterfaces;
        this.uml_tracedreceptions = uml_tracedreceptions;
        this.uml_tracedpropertys = uml_tracedpropertys;
        this.uml_tracedclassifiers = uml_tracedclassifiers;
    }


    public List<uml_TracedOperation> getUml_tracedoperations() {
        return uml_tracedoperations;
    }

    public void addUml_tracedoperation(Uml_tracedoperation uml_tracedoperation) {
        this.uml_tracedoperations.add(uml_tracedoperation);
    }
    public List<uml_TracedInterface> getUml_tracedinterfaces() {
        return uml_tracedinterfaces;
    }

    public void addUml_tracedinterface(Uml_tracedinterface uml_tracedinterface) {
        this.uml_tracedinterfaces.add(uml_tracedinterface);
    }
    public uml_TracedProtocolStateMachine getUml_tracedprotocolstatemachine() {
        return uml_tracedprotocolstatemachine;
    }

    public void setUml_tracedprotocolstatemachine(uml_TracedProtocolStateMachine uml_tracedprotocolstatemachine) {
        this.uml_tracedprotocolstatemachine = uml_tracedprotocolstatemachine;
    }
    public List<uml_TracedReception> getUml_tracedreceptions() {
        return uml_tracedreceptions;
    }

    public void addUml_tracedreception(Uml_tracedreception uml_tracedreception) {
        this.uml_tracedreceptions.add(uml_tracedreception);
    }
    public List<uml_TracedProperty> getUml_tracedpropertys() {
        return uml_tracedpropertys;
    }

    public void addUml_tracedproperty(Uml_tracedproperty uml_tracedproperty) {
        this.uml_tracedpropertys.add(uml_tracedproperty);
    }
    public List<uml_TracedClassifier> getUml_tracedclassifiers() {
        return uml_tracedclassifiers;
    }

    public void addUml_tracedclassifier(Uml_tracedclassifier uml_tracedclassifier) {
        this.uml_tracedclassifiers.add(uml_tracedclassifier);
    }

}