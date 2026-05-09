





import java.util.List;
import java.util.ArrayList;

public class gastm_DataDefinition extends Definition {

    private String isMutable;





    private gastm_Expression gastm_expression;


    public gastm_DataDefinition(
        String isMutable    ) {
        super(
        );
        this.isMutable = isMutable;
    }


    public String getIsmutable() {
        return isMutable;
    }

    public void setIsmutable(String isMutable) {
        this.isMutable = isMutable;
    }

    public gastm_Expression getGastm_expression() {
        return gastm_expression;
    }

    public void setGastm_expression(gastm_Expression gastm_expression) {
        this.gastm_expression = gastm_expression;
    }

}