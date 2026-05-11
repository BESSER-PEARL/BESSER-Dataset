





import java.util.List;
import java.util.ArrayList;

public class modelDsl_DefSimpleVariable extends DefAttribute, DefVariable, DefIdAttribute {

    private String type;
    private String nullable;



    public modelDsl_DefSimpleVariable(
        String type,        String nullable    ) {
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
    public String getNullable() {
        return nullable;
    }

    public void setNullable(String nullable) {
        this.nullable = nullable;
    }


}