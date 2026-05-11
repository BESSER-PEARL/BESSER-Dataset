





import java.util.List;
import java.util.ArrayList;

public class selflet_CPUUtilization  {

    private String lowerBound;
    private String upperBound;



    public selflet_CPUUtilization(
        String lowerBound,        String upperBound    ) {
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public String getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(String lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }


}