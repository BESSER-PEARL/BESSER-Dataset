





import java.util.List;
import java.util.ArrayList;

public class simulink_PortBlock extends Block {

    private String dimensions;
    private String type;
    private String initialCondition;



    public simulink_PortBlock(
        String dimensions,        String type,        String initialCondition    ) {
        super(
        );
        this.dimensions = dimensions;
        this.type = type;
        this.initialCondition = initialCondition;
    }


    public String getDimensions() {
        return dimensions;
    }

    public void setDimensions(String dimensions) {
        this.dimensions = dimensions;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getInitialcondition() {
        return initialCondition;
    }

    public void setInitialcondition(String initialCondition) {
        this.initialCondition = initialCondition;
    }


}