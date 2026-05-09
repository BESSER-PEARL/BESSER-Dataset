





import java.util.List;
import java.util.ArrayList;

public class eTJ_LogicalFlagExpression extends LogicalExpression {

    private String columId;



    public eTJ_LogicalFlagExpression(
        String columId    ) {
        super(
        );
        this.columId = columId;
    }


    public String getColumid() {
        return columId;
    }

    public void setColumid(String columId) {
        this.columId = columId;
    }


}