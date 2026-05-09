





import java.util.List;
import java.util.ArrayList;

public class dom_NumericLiteral extends IPropertyName, Expression {

    private String text;



    public dom_NumericLiteral(
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