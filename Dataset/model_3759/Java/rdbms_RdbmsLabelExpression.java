





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsLabelExpression extends RdbmsExpression {

    private String text;



    public rdbms_RdbmsLabelExpression(
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