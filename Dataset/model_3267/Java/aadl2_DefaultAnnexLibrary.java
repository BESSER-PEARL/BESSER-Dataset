





import java.util.List;
import java.util.ArrayList;

public class aadl2_DefaultAnnexLibrary extends AnnexLibrary {

    private String sourceText;





    private aadl2_AnnexLibrary aadl2_annexlibrary;


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

    public aadl2_AnnexLibrary getAadl2_annexlibrary() {
        return aadl2_annexlibrary;
    }

    public void setAadl2_annexlibrary(aadl2_AnnexLibrary aadl2_annexlibrary) {
        this.aadl2_annexlibrary = aadl2_annexlibrary;
    }

}