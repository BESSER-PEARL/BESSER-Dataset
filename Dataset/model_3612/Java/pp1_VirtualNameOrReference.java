





import java.util.List;
import java.util.ArrayList;

public class pp1_VirtualNameOrReference extends LiteralExpression {

    private String value;
    private boolean exported;



    public pp1_VirtualNameOrReference(
        String value,        boolean exported    ) {
        super(
        );
        this.value = value;
        this.exported = exported;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getExported() {
        return exported;
    }

    public void setExported(boolean exported) {
        this.exported = exported;
    }


}