





import java.util.List;
import java.util.ArrayList;

public class expressionDSL_SubFieldDef extends Named, SubField {

    private String type;



    public expressionDSL_SubFieldDef(
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