





import java.util.List;
import java.util.ArrayList;

public class roverDSL_ColorLiteral extends ValueExpression {

    private String color;



    public roverDSL_ColorLiteral(
        String color    ) {
        super(
        );
        this.color = color;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}