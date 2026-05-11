





import java.util.List;
import java.util.ArrayList;

public class iec61131_st_Expression_EnumValue extends Primary_Expression {






    private Enumerated_Value enumerated_value;


    public iec61131_st_Expression_EnumValue(
    ) {
        super(
        );
    }



    public Enumerated_Value getEnumerated_value() {
        return enumerated_value;
    }

    public void setEnumerated_value(Enumerated_Value enumerated_value) {
        this.enumerated_value = enumerated_value;
    }

}