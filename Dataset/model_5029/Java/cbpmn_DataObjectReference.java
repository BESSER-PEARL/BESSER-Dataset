





import java.util.List;
import java.util.ArrayList;

public class cbpmn_DataObjectReference  {

    private int lowerBound;
    private String name;
    private int higherBound;



    public cbpmn_DataObjectReference(
        int lowerBound,        String name,        int higherBound    ) {
        this.lowerBound = lowerBound;
        this.name = name;
        this.higherBound = higherBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getHigherbound() {
        return higherBound;
    }

    public void setHigherbound(int higherBound) {
        this.higherBound = higherBound;
    }


}