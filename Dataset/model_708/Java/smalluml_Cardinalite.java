





import java.util.List;
import java.util.ArrayList;

public class smalluml_Cardinalite extends NamedElement {

    private String upperBound;
    private String lowerBound;



    public smalluml_Cardinalite(
        String upperBound,        String lowerBound    ) {
        super(
        );
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