





import java.util.List;
import java.util.ArrayList;

public class ir_ActorInstance extends Variable {






    private List<ir_PortInstance> ir_portinstances;




    private ir_PortInstance ir_portinstance;




    private List<ir_PortInstance> ir_portinstances;




    private List<ir_TaggedExpression> ir_taggedexpressions;




    private ir_Network ir_network;


    public ir_ActorInstance(
    ) {
        super(
        );
        this.ir_portinstances = new ArrayList<>();
        this.ir_portinstances = new ArrayList<>();
        this.ir_taggedexpressions = new ArrayList<>();
    }

    public ir_ActorInstance(
        ArrayList<ir_PortInstance> ir_portinstances,        ArrayList<ir_PortInstance> ir_portinstances,        ArrayList<ir_TaggedExpression> ir_taggedexpressions    ) {
        this.ir_portinstances = ir_portinstances;
        this.ir_portinstances = ir_portinstances;
        this.ir_taggedexpressions = ir_taggedexpressions;
    }


    public List<ir_PortInstance> getIr_portinstances() {
        return ir_portinstances;
    }

    public void addIr_portinstance(Ir_portinstance ir_portinstance) {
        this.ir_portinstances.add(ir_portinstance);
    }
    public ir_PortInstance getIr_portinstance() {
        return ir_portinstance;
    }

    public void setIr_portinstance(ir_PortInstance ir_portinstance) {
        this.ir_portinstance = ir_portinstance;
    }
    public List<ir_PortInstance> getIr_portinstances() {
        return ir_portinstances;
    }

    public void addIr_portinstance(Ir_portinstance ir_portinstance) {
        this.ir_portinstances.add(ir_portinstance);
    }
    public List<ir_TaggedExpression> getIr_taggedexpressions() {
        return ir_taggedexpressions;
    }

    public void addIr_taggedexpression(Ir_taggedexpression ir_taggedexpression) {
        this.ir_taggedexpressions.add(ir_taggedexpression);
    }
    public ir_Network getIr_network() {
        return ir_network;
    }

    public void setIr_network(ir_Network ir_network) {
        this.ir_network = ir_network;
    }

}