





import java.util.List;
import java.util.ArrayList;

public class gpfl_SendCmd extends GExpression {






    private List<gpfl_Field> gpfl_fields;




    private gpfl_GExpression gpfl_gexpression;


    public gpfl_SendCmd(
    ) {
        super(
        );
        this.gpfl_fields = new ArrayList<>();
    }

    public gpfl_SendCmd(
        ArrayList<gpfl_Field> gpfl_fields    ) {
        this.gpfl_fields = gpfl_fields;
    }


    public List<gpfl_Field> getGpfl_fields() {
        return gpfl_fields;
    }

    public void addGpfl_field(Gpfl_field gpfl_field) {
        this.gpfl_fields.add(gpfl_field);
    }
    public gpfl_GExpression getGpfl_gexpression() {
        return gpfl_gexpression;
    }

    public void setGpfl_gexpression(gpfl_GExpression gpfl_gexpression) {
        this.gpfl_gexpression = gpfl_gexpression;
    }

}