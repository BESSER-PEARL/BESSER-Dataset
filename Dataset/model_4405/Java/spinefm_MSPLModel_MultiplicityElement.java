





import java.util.List;
import java.util.ArrayList;

public class spinefm_MSPLModel_MultiplicityElement  {

    private int lowerBound;
    private String id;
    private int upperBound;



    public spinefm_MSPLModel_MultiplicityElement(
        int lowerBound,        String id,        int upperBound    ) {
        this.lowerBound = lowerBound;
        this.id = id;
        this.upperBound = upperBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }


}