





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaAnalysisContext extends CoreElements_Configuration, Variables_ExpressionContext {






    private List<NFP_String> nfp_strings;


    public MARTE_GQAM_GaAnalysisContext(
    ) {
        super(
        );
        this.nfp_strings = new ArrayList<>();
    }

    public MARTE_GQAM_GaAnalysisContext(
        ArrayList<NFP_String> nfp_strings    ) {
        this.nfp_strings = nfp_strings;
    }


    public List<NFP_String> getNfp_strings() {
        return nfp_strings;
    }

    public void addNfp_string(Nfp_string nfp_string) {
        this.nfp_strings.add(nfp_string);
    }

}