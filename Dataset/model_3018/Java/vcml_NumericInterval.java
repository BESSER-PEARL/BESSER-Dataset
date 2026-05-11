





import java.util.List;
import java.util.ArrayList;

public class vcml_NumericInterval extends NumberListEntry {

    private String lowerBound;
    private String upperBoundOp;
    private String upperBound;
    private String lowerBoundOp;



    public vcml_NumericInterval(
        String lowerBound,        String upperBoundOp,        String upperBound,        String lowerBoundOp    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.upperBoundOp = upperBoundOp;
        this.upperBound = upperBound;
        this.lowerBoundOp = lowerBoundOp;
    }


    public String getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(String lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getUpperboundop() {
        return upperBoundOp;
    }

    public void setUpperboundop(String upperBoundOp) {
        this.upperBoundOp = upperBoundOp;
    }
    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }
    public String getLowerboundop() {
        return lowerBoundOp;
    }

    public void setLowerboundop(String lowerBoundOp) {
        this.lowerBoundOp = lowerBoundOp;
    }


}