





import java.util.List;
import java.util.ArrayList;

public class ea_extensions_StringExtension extends ExtensionElement {

    private String value;



    public ea_extensions_StringExtension(
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