





import java.util.List;
import java.util.ArrayList;

public class qvtimperativecs_MappingCS extends AbstractMappingCS {






    private List<qvtimperativecs_PathNameCS> qvtimperativecs_pathnamecss;




    private qvtimperativecs_MappingSequenceCS qvtimperativecs_mappingsequencecs;


    public qvtimperativecs_MappingCS(
    ) {
        super(
        );
        this.qvtimperativecs_pathnamecss = new ArrayList<>();
    }

    public qvtimperativecs_MappingCS(
        ArrayList<qvtimperativecs_PathNameCS> qvtimperativecs_pathnamecss    ) {
        this.qvtimperativecs_pathnamecss = qvtimperativecs_pathnamecss;
    }


    public List<qvtimperativecs_PathNameCS> getQvtimperativecs_pathnamecss() {
        return qvtimperativecs_pathnamecss;
    }

    public void addQvtimperativecs_pathnamecs(Qvtimperativecs_pathnamecs qvtimperativecs_pathnamecs) {
        this.qvtimperativecs_pathnamecss.add(qvtimperativecs_pathnamecs);
    }
    public qvtimperativecs_MappingSequenceCS getQvtimperativecs_mappingsequencecs() {
        return qvtimperativecs_mappingsequencecs;
    }

    public void setQvtimperativecs_mappingsequencecs(qvtimperativecs_MappingSequenceCS qvtimperativecs_mappingsequencecs) {
        this.qvtimperativecs_mappingsequencecs = qvtimperativecs_mappingsequencecs;
    }

}