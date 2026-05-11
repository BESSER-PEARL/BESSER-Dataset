





import java.util.List;
import java.util.ArrayList;

public class etricegen_ActorInstance extends StructureInstance {

    private String unindexedName;
    private int replIdx;





    private etricegen_StructureInstance etricegen_structureinstance;




    private etricegen_ActorClass etricegen_actorclass;


    public etricegen_ActorInstance(
        String unindexedName,        int replIdx    ) {
        super(
        );
        this.unindexedName = unindexedName;
        this.replIdx = replIdx;
    }


    public String getUnindexedname() {
        return unindexedName;
    }

    public void setUnindexedname(String unindexedName) {
        this.unindexedName = unindexedName;
    }
    public int getReplidx() {
        return replIdx;
    }

    public void setReplidx(int replIdx) {
        this.replIdx = replIdx;
    }

    public etricegen_StructureInstance getEtricegen_structureinstance() {
        return etricegen_structureinstance;
    }

    public void setEtricegen_structureinstance(etricegen_StructureInstance etricegen_structureinstance) {
        this.etricegen_structureinstance = etricegen_structureinstance;
    }
    public etricegen_ActorClass getEtricegen_actorclass() {
        return etricegen_actorclass;
    }

    public void setEtricegen_actorclass(etricegen_ActorClass etricegen_actorclass) {
        this.etricegen_actorclass = etricegen_actorclass;
    }

}