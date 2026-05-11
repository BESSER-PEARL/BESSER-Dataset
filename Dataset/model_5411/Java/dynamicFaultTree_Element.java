





import java.util.List;
import java.util.ArrayList;

public class dynamicFaultTree_Element  {

    private int elementID;
    private float probability;
    private int sequencePosition;
    private String name;



    public dynamicFaultTree_Element(
        int elementID,        float probability,        int sequencePosition,        String name    ) {
        this.elementID = elementID;
        this.probability = probability;
        this.sequencePosition = sequencePosition;
        this.name = name;
    }


    public int getElementid() {
        return elementID;
    }

    public void setElementid(int elementID) {
        this.elementID = elementID;
    }
    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }
    public int getSequenceposition() {
        return sequencePosition;
    }

    public void setSequenceposition(int sequencePosition) {
        this.sequencePosition = sequencePosition;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}