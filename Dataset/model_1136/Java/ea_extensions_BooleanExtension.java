





import java.util.List;
import java.util.ArrayList;

public class ea_extensions_BooleanExtension extends ExtensionElement {

    private boolean value;



    public ea_extensions_BooleanExtension(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}