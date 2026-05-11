





import java.util.List;
import java.util.ArrayList;

public class vhdl_type_PhysicalTypeDefinition extends TypeDefinition {

    private String primary;





    private Expression expression;


    public vhdl_type_PhysicalTypeDefinition(
        String primary    ) {
        super(
        );
        this.primary = primary;
    }


    public String getPrimary() {
        return primary;
    }

    public void setPrimary(String primary) {
        this.primary = primary;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}