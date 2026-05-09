





import java.util.List;
import java.util.ArrayList;

public class syswbeff106_SequenceNode  {

    private int tMin;
    private int tMax;
    private String name;





    private List<syswbeff106_SequenceNode> syswbeff106_sequencenodes;


    public syswbeff106_SequenceNode(
        int tMin,        int tMax,        String name    ) {
        this.tMin = tMin;
        this.tMax = tMax;
        this.name = name;
        this.syswbeff106_sequencenodes = new ArrayList<>();
    }

    public syswbeff106_SequenceNode(
        int tMin,        int tMax,        String name        ArrayList<syswbeff106_SequenceNode> syswbeff106_sequencenodes    ) {
        this.tMin = tMin;
        this.tMax = tMax;
        this.name = name;
        this.syswbeff106_sequencenodes = syswbeff106_sequencenodes;
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

    public List<syswbeff106_SequenceNode> getSyswbeff106_sequencenodes() {
        return syswbeff106_sequencenodes;
    }

    public void addSyswbeff106_sequencenode(Syswbeff106_sequencenode syswbeff106_sequencenode) {
        this.syswbeff106_sequencenodes.add(syswbeff106_sequencenode);
    }

}