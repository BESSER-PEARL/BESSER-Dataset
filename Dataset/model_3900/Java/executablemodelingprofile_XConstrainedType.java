





import java.util.List;
import java.util.ArrayList;

public class executablemodelingprofile_XConstrainedType extends XClassifier {

    private String isLowerBoundExclusive;
    private String isUpperBoundExclusive;



    public executablemodelingprofile_XConstrainedType(
        String isLowerBoundExclusive,        String isUpperBoundExclusive    ) {
        super(
        );
        this.isLowerBoundExclusive = isLowerBoundExclusive;
        this.isUpperBoundExclusive = isUpperBoundExclusive;
    }


    public String getIslowerboundexclusive() {
        return isLowerBoundExclusive;
    }

    public void setIslowerboundexclusive(String isLowerBoundExclusive) {
        this.isLowerBoundExclusive = isLowerBoundExclusive;
    }
    public String getIsupperboundexclusive() {
        return isUpperBoundExclusive;
    }

    public void setIsupperboundexclusive(String isUpperBoundExclusive) {
        this.isUpperBoundExclusive = isUpperBoundExclusive;
    }


}