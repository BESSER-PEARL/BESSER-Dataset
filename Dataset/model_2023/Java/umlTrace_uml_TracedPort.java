





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedPort extends TracedProperty {






    private uml_TracedProtocolStateMachine uml_tracedprotocolstatemachine;




    private List<uml_TracedInterface> uml_tracedinterfaces;




    private List<uml_TracedPort> uml_tracedports;




    private List<uml_TracedInterface> uml_tracedinterfaces;


    public umlTrace_uml_TracedPort(
    ) {
        super(
        );
        this.uml_tracedinterfaces = new ArrayList<>();
        this.uml_tracedports = new ArrayList<>();
        this.uml_tracedinterfaces = new ArrayList<>();
    }

    public umlTrace_uml_TracedPort(
        ArrayList<uml_TracedInterface> uml_tracedinterfaces,        ArrayList<uml_TracedPort> uml_tracedports,        ArrayList<uml_TracedInterface> uml_tracedinterfaces    ) {
        this.uml_tracedinterfaces = uml_tracedinterfaces;
        this.uml_tracedports = uml_tracedports;
        this.uml_tracedinterfaces = uml_tracedinterfaces;
    }


    public uml_TracedProtocolStateMachine getUml_tracedprotocolstatemachine() {
        return uml_tracedprotocolstatemachine;
    }

    public void setUml_tracedprotocolstatemachine(uml_TracedProtocolStateMachine uml_tracedprotocolstatemachine) {
        this.uml_tracedprotocolstatemachine = uml_tracedprotocolstatemachine;
    }
    public List<uml_TracedInterface> getUml_tracedinterfaces() {
        return uml_tracedinterfaces;
    }

    public void addUml_tracedinterface(Uml_tracedinterface uml_tracedinterface) {
        this.uml_tracedinterfaces.add(uml_tracedinterface);
    }
    public List<uml_TracedPort> getUml_tracedports() {
        return uml_tracedports;
    }

    public void addUml_tracedport(Uml_tracedport uml_tracedport) {
        this.uml_tracedports.add(uml_tracedport);
    }
    public List<uml_TracedInterface> getUml_tracedinterfaces() {
        return uml_tracedinterfaces;
    }

    public void addUml_tracedinterface(Uml_tracedinterface uml_tracedinterface) {
        this.uml_tracedinterfaces.add(uml_tracedinterface);
    }

}