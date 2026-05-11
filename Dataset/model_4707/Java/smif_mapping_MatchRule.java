





import java.util.List;
import java.util.ArrayList;

public class smif_mapping_MatchRule extends Rule {

    private String coerce;



    public smif_mapping_MatchRule(
        String coerce    ) {
        super(
        );
        this.coerce = coerce;
    }


    public String getCoerce() {
        return coerce;
    }

    public void setCoerce(String coerce) {
        this.coerce = coerce;
    }


}