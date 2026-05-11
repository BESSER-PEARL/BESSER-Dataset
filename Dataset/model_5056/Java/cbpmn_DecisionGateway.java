





import java.util.List;
import java.util.ArrayList;

public class cbpmn_DecisionGateway extends SplitGateway {

    private String type;



    public cbpmn_DecisionGateway(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}