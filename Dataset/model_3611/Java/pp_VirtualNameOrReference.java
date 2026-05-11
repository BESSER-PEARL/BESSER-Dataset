





import java.util.List;
import java.util.ArrayList;

public class pp_VirtualNameOrReference extends LiteralExpression {

    private boolean exported;
    private String value;



    public pp_VirtualNameOrReference(
        boolean exported,        String value    ) {
        super(
        );
        this.exported = exported;
        this.value = value;
    }


    public boolean getExported() {
        return exported;
    }

    public void setExported(boolean exported) {
        this.exported = exported;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}