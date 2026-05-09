





import java.util.List;
import java.util.ArrayList;

public class simulink_stateflow_EmbeddedFunction extends StateflowElement {

    private String code;
    private String name;



    public simulink_stateflow_EmbeddedFunction(
        String code,        String name    ) {
        super(
        );
        this.code = code;
        this.name = name;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}