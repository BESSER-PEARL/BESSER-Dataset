





import java.util.List;
import java.util.ArrayList;

public class aadl2_DefaultAnnexLibrary extends AnnexLibrary {

    private String sourceText;



    public aadl2_DefaultAnnexLibrary(
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