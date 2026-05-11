





import java.util.List;
import java.util.ArrayList;

public class uppaal_expressions_DataPrefixExpression extends Expression {

    private String prefix;



    public uppaal_expressions_DataPrefixExpression(
        String prefix    ) {
        super(
        );
        this.prefix = prefix;
    }


    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }


}