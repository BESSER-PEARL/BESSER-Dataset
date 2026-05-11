





import java.util.List;
import java.util.ArrayList;

public class smif_identifiers_TextIdentifier extends Identifier {

    private String value;



    public smif_identifiers_TextIdentifier(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}