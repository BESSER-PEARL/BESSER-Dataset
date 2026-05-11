





import java.util.List;
import java.util.ArrayList;

public class uppaal_expressions_LiteralExpression extends Expression {

    private String text;



    public uppaal_expressions_LiteralExpression(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}