





import java.util.List;
import java.util.ArrayList;

public class KragsteinPackage_Relationship  {

    private int upperBound;
    private String name;
    private int lowerBound;



    public KragsteinPackage_Relationship(
        int upperBound,        String name,        int lowerBound    ) {
        this.upperBound = upperBound;
        this.name = name;
        this.lowerBound = lowerBound;
    }


    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }


}