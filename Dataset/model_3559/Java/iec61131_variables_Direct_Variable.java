





import java.util.List;
import java.util.ArrayList;

public class iec61131_variables_Direct_Variable extends configurations_Data_Sink, configurations_Prog_Data_Source, variables_Variable, configurations_Data_Source {

    private String value;



    public iec61131_variables_Direct_Variable(
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