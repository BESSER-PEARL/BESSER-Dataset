





import java.util.List;
import java.util.ArrayList;

public class ea_extensions_IntegerExtension extends ExtensionElement {

    private int value;



    public ea_extensions_IntegerExtension(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}