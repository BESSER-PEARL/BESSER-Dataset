





import java.util.List;
import java.util.ArrayList;

public class stext_Operation extends Declaration {

    private String paramTypes;
    private String type;



    public stext_Operation(
        String paramTypes,        String type    ) {
        super(
        );
        this.paramTypes = paramTypes;
        this.type = type;
    }


    public String getParamtypes() {
        return paramTypes;
    }

    public void setParamtypes(String paramTypes) {
        this.paramTypes = paramTypes;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}