





import java.util.List;
import java.util.ArrayList;

public class SPL_SimpleType extends TypeExpression {

    private String type;



    public SPL_SimpleType(
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