





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_OneOf extends DiagnosticParamValueType {

    private String values;



    public DiagonosticModel_OneOf(
        String values    ) {
        super(
        );
        this.values = values;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }


}