





import java.util.List;
import java.util.ArrayList;

public class aS3_Uses  {

    private String type;
    private String anytype;





    private aS3_directive as3_directive;


    public aS3_Uses(
        String type,        String anytype    ) {
        this.type = type;
        this.anytype = anytype;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAnytype() {
        return anytype;
    }

    public void setAnytype(String anytype) {
        this.anytype = anytype;
    }

    public aS3_directive getAs3_directive() {
        return as3_directive;
    }

    public void setAs3_directive(aS3_directive as3_directive) {
        this.as3_directive = as3_directive;
    }

}