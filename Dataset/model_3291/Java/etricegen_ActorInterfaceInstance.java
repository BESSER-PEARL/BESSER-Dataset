





import java.util.List;
import java.util.ArrayList;

public class etricegen_ActorInterfaceInstance extends AbstractInstance {

    private boolean array;





    private etricegen_ActorClass etricegen_actorclass;




    private List<etricegen_OptionalActorInstance> etricegen_optionalactorinstances;


    public etricegen_ActorInterfaceInstance(
        boolean array    ) {
        super(
        );
        this.array = array;
        this.etricegen_optionalactorinstances = new ArrayList<>();
    }

    public etricegen_ActorInterfaceInstance(
        boolean array        ArrayList<etricegen_OptionalActorInstance> etricegen_optionalactorinstances    ) {
        this.array = array;
        this.etricegen_optionalactorinstances = etricegen_optionalactorinstances;
    }

    public boolean getArray() {
        return array;
    }

    public void setArray(boolean array) {
        this.array = array;
    }

    public etricegen_ActorClass getEtricegen_actorclass() {
        return etricegen_actorclass;
    }

    public void setEtricegen_actorclass(etricegen_ActorClass etricegen_actorclass) {
        this.etricegen_actorclass = etricegen_actorclass;
    }
    public List<etricegen_OptionalActorInstance> getEtricegen_optionalactorinstances() {
        return etricegen_optionalactorinstances;
    }

    public void addEtricegen_optionalactorinstance(Etricegen_optionalactorinstance etricegen_optionalactorinstance) {
        this.etricegen_optionalactorinstances.add(etricegen_optionalactorinstance);
    }

}