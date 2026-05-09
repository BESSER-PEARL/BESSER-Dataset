





import java.util.List;
import java.util.ArrayList;

public class gpfl_SetCmd extends GExpression {

    private String name;





    private gpfl_GExpression gpfl_gexpression;


    public gpfl_SetCmd(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gpfl_GExpression getGpfl_gexpression() {
        return gpfl_gexpression;
    }

    public void setGpfl_gexpression(gpfl_GExpression gpfl_gexpression) {
        this.gpfl_gexpression = gpfl_gexpression;
    }

}