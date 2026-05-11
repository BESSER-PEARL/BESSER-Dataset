





import java.util.List;
import java.util.ArrayList;

public class gaml_Parameter extends Expression {

    private String builtInFacetKey;



    public gaml_Parameter(
        String builtInFacetKey    ) {
        super(
        );
        this.builtInFacetKey = builtInFacetKey;
    }


    public String getBuiltinfacetkey() {
        return builtInFacetKey;
    }

    public void setBuiltinfacetkey(String builtInFacetKey) {
        this.builtInFacetKey = builtInFacetKey;
    }


}