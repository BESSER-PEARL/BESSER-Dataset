





import java.util.List;
import java.util.ArrayList;

public class fIDL_HandleType extends Type {

    private String type;
    private boolean nullable;



    public fIDL_HandleType(
        String type,        boolean nullable    ) {
        super(
        );
        this.type = type;
        this.nullable = nullable;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }


}