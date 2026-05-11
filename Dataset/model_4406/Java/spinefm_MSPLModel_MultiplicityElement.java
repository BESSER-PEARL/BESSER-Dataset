





import java.util.List;
import java.util.ArrayList;

public class spinefm_MSPLModel_MultiplicityElement  {

    private String id;
    private int lowerBound;
    private int upperBound;



    public spinefm_MSPLModel_MultiplicityElement(
        String id,        int lowerBound,        int upperBound    ) {
        this.id = id;
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }


}