





import java.util.List;
import java.util.ArrayList;

public class vhdl_expression_RangeExpression extends expression_BinaryExpression, Name {

    private String direction;



    public vhdl_expression_RangeExpression(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}