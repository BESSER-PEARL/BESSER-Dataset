





import java.util.List;
import java.util.ArrayList;

public class aadl2_DefaultAnnexSubclause extends AnnexSubclause {

    private String sourceText;





    private aadl2_AnnexSubclause aadl2_annexsubclause;


    public aadl2_DefaultAnnexSubclause(
        String sourceText    ) {
        super(
        );
        this.sourceText = sourceText;
    }


    public String getSourcetext() {
        return sourceText;
    }

    public void setSourcetext(String sourceText) {
        this.sourceText = sourceText;
    }

    public aadl2_AnnexSubclause getAadl2_annexsubclause() {
        return aadl2_annexsubclause;
    }

    public void setAadl2_annexsubclause(aadl2_AnnexSubclause aadl2_annexsubclause) {
        this.aadl2_annexsubclause = aadl2_annexsubclause;
    }

}