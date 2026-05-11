





import java.util.List;
import java.util.ArrayList;

public class p2_TouchpointData extends ITouchpointData {






    private List<p2_InstructionMap> p2_instructionmaps;


    public p2_TouchpointData(
    ) {
        super(
        );
        this.p2_instructionmaps = new ArrayList<>();
    }

    public p2_TouchpointData(
        ArrayList<p2_InstructionMap> p2_instructionmaps    ) {
        this.p2_instructionmaps = p2_instructionmaps;
    }


    public List<p2_InstructionMap> getP2_instructionmaps() {
        return p2_instructionmaps;
    }

    public void addP2_instructionmap(P2_instructionmap p2_instructionmap) {
        this.p2_instructionmaps.add(p2_instructionmap);
    }

}