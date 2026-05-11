





import java.util.List;
import java.util.ArrayList;

public class aadl2_DefaultAnnexSubclause extends AnnexSubclause {

    private String sourceText;



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


}