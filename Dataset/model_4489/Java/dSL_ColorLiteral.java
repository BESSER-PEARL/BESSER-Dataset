





import java.util.List;
import java.util.ArrayList;

public class dSL_ColorLiteral extends Expression {

    private String color;



    public dSL_ColorLiteral(
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