





import java.util.List;
import java.util.ArrayList;

public class expressionDSL_VariableDef extends Named, Statement {

    private String type;



    public expressionDSL_VariableDef(
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