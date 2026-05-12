





import java.util.List;
import java.util.ArrayList;

public class stext_Operation extends Declaration {

    private String type;
    private String paramTypes;



    public stext_Operation(
        String type,        String paramTypes    ) {
        super(
        );
        this.type = type;
        this.paramTypes = paramTypes;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getParamtypes() {
        return paramTypes;
    }

    public void setParamtypes(String paramTypes) {
        this.paramTypes = paramTypes;
    }


}