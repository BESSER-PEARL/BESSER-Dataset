





import java.util.List;
import java.util.ArrayList;

public class aadl2_ArrayRange extends Element {

    private String lowerBound;
    private String upperBound;





    private aadl2_ContainmentPathElement aadl2_containmentpathelement;


    public aadl2_ArrayRange(
        String lowerBound,        String upperBound    ) {
        super(
        );
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

    public aadl2_ContainmentPathElement getAadl2_containmentpathelement() {
        return aadl2_containmentpathelement;
    }

    public void setAadl2_containmentpathelement(aadl2_ContainmentPathElement aadl2_containmentpathelement) {
        this.aadl2_containmentpathelement = aadl2_containmentpathelement;
    }

}