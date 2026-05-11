





import java.util.List;
import java.util.ArrayList;

public class nuSMV_ArrayType extends SimpleType {

    private String lowerBound;
    private String upperBound;





    private nuSMV_SimpleType nusmv_simpletype;


    public nuSMV_ArrayType(
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

    public nuSMV_SimpleType getNusmv_simpletype() {
        return nusmv_simpletype;
    }

    public void setNusmv_simpletype(nuSMV_SimpleType nusmv_simpletype) {
        this.nusmv_simpletype = nusmv_simpletype;
    }

}