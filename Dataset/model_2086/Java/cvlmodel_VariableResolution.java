





import java.util.List;
import java.util.ArrayList;

public class cvlmodel_VariableResolution extends VSpecResolution {

    private String value;



    public cvlmodel_VariableResolution(
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