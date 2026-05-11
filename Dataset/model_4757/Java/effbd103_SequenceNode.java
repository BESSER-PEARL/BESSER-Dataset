





import java.util.List;
import java.util.ArrayList;

public class effbd103_SequenceNode  {

    private int tMin;
    private int tMax;
    private String name;





    private effbd103_SequenceNode effbd103_sequencenode;


    public effbd103_SequenceNode(
        int tMin,        int tMax,        String name    ) {
        this.tMin = tMin;
        this.tMax = tMax;
        this.name = name;
    }


    public int getTmin() {
        return tMin;
    }

    public void setTmin(int tMin) {
        this.tMin = tMin;
    }
    public int getTmax() {
        return tMax;
    }

    public void setTmax(int tMax) {
        this.tMax = tMax;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public effbd103_SequenceNode getEffbd103_sequencenode() {
        return effbd103_sequencenode;
    }

    public void setEffbd103_sequencenode(effbd103_SequenceNode effbd103_sequencenode) {
        this.effbd103_sequencenode = effbd103_sequencenode;
    }

}