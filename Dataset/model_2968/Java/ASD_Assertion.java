





import java.util.List;
import java.util.ArrayList;

public class ASD_Assertion extends NamedElement {

    private String dimensionType;
    private String dimension;
    private String subset;
    private float maxVal;
    private String lType;
    private String role;
    private float minVal;





    private ASD_AssertionSet asd_assertionset;




    private ASD_AssertionSet asd_assertionset;


    public ASD_Assertion(
        String dimensionType,        String dimension,        String subset,        float maxVal,        String lType,        String role,        float minVal    ) {
        super(
        );
        this.dimensionType = dimensionType;
        this.dimension = dimension;
        this.subset = subset;
        this.maxVal = maxVal;
        this.lType = lType;
        this.role = role;
        this.minVal = minVal;
    }


    public String getDimensiontype() {
        return dimensionType;
    }

    public void setDimensiontype(String dimensionType) {
        this.dimensionType = dimensionType;
    }
    public String getDimension() {
        return dimension;
    }

    public void setDimension(String dimension) {
        this.dimension = dimension;
    }
    public String getSubset() {
        return subset;
    }

    public void setSubset(String subset) {
        this.subset = subset;
    }
    public float getMaxval() {
        return maxVal;
    }

    public void setMaxval(float maxVal) {
        this.maxVal = maxVal;
    }
    public String getLtype() {
        return lType;
    }

    public void setLtype(String lType) {
        this.lType = lType;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public float getMinval() {
        return minVal;
    }

    public void setMinval(float minVal) {
        this.minVal = minVal;
    }

    public ASD_AssertionSet getAsd_assertionset() {
        return asd_assertionset;
    }

    public void setAsd_assertionset(ASD_AssertionSet asd_assertionset) {
        this.asd_assertionset = asd_assertionset;
    }
    public ASD_AssertionSet getAsd_assertionset() {
        return asd_assertionset;
    }

    public void setAsd_assertionset(ASD_AssertionSet asd_assertionset) {
        this.asd_assertionset = asd_assertionset;
    }

}