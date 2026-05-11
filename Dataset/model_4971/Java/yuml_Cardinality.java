





import java.util.List;
import java.util.ArrayList;

public class yuml_Cardinality  {

    private String lowerBound;
    private String upperBound;





    private yuml_Association yuml_association;




    private yuml_Association yuml_association;


    public yuml_Cardinality(
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

    public yuml_Association getYuml_association() {
        return yuml_association;
    }

    public void setYuml_association(yuml_Association yuml_association) {
        this.yuml_association = yuml_association;
    }
    public yuml_Association getYuml_association() {
        return yuml_association;
    }

    public void setYuml_association(yuml_Association yuml_association) {
        this.yuml_association = yuml_association;
    }

}