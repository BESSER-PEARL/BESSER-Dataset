





import java.util.List;
import java.util.ArrayList;

public class UsecaseDSL_MultiplicityElement_c  {

    private String targetLower;
    private String sourceLower;
    private String sourceUpper;
    private String targetUpper;



    public UsecaseDSL_MultiplicityElement_c(
        String targetLower,        String sourceLower,        String sourceUpper,        String targetUpper    ) {
        this.targetLower = targetLower;
        this.sourceLower = sourceLower;
        this.sourceUpper = sourceUpper;
        this.targetUpper = targetUpper;
    }


    public String getTargetlower() {
        return targetLower;
    }

    public void setTargetlower(String targetLower) {
        this.targetLower = targetLower;
    }
    public String getSourcelower() {
        return sourceLower;
    }

    public void setSourcelower(String sourceLower) {
        this.sourceLower = sourceLower;
    }
    public String getSourceupper() {
        return sourceUpper;
    }

    public void setSourceupper(String sourceUpper) {
        this.sourceUpper = sourceUpper;
    }
    public String getTargetupper() {
        return targetUpper;
    }

    public void setTargetupper(String targetUpper) {
        this.targetUpper = targetUpper;
    }


}