





import java.util.List;
import java.util.ArrayList;

public class selflet_CPUUtilization  {

    private String upperBound;
    private String lowerBound;



    public selflet_CPUUtilization(
        String upperBound,        String lowerBound    ) {
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
    }


    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }
    public String getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(String lowerBound) {
        this.lowerBound = lowerBound;
    }


}