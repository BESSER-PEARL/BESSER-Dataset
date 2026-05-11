





import java.util.List;
import java.util.ArrayList;

public class ioT_Variable extends VarOrList {






    private ioT_ReadVariable iot_readvariable;




    private ioT_Expression iot_expression;




    private ioT_ToVar iot_tovar;


    public ioT_Variable(
    ) {
        super(
        );
    }



    public ioT_ReadVariable getIot_readvariable() {
        return iot_readvariable;
    }

    public void setIot_readvariable(ioT_ReadVariable iot_readvariable) {
        this.iot_readvariable = iot_readvariable;
    }
    public ioT_Expression getIot_expression() {
        return iot_expression;
    }

    public void setIot_expression(ioT_Expression iot_expression) {
        this.iot_expression = iot_expression;
    }
    public ioT_ToVar getIot_tovar() {
        return iot_tovar;
    }

    public void setIot_tovar(ioT_ToVar iot_tovar) {
        this.iot_tovar = iot_tovar;
    }

}