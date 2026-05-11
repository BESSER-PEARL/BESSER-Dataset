





import java.util.List;
import java.util.ArrayList;

public class dot_AttributeStatement extends Statement {

    private String type;



    public dot_AttributeStatement(
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