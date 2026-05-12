





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CastExpression extends Expression {

    private String type;



    public sqliteModel_CastExpression(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}