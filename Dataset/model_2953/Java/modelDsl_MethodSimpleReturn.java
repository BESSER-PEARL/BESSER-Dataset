





import java.util.List;
import java.util.ArrayList;

public class modelDsl_MethodSimpleReturn extends Method {

    private String returnType;



    public modelDsl_MethodSimpleReturn(
        String returnType    ) {
        super(
        );
        this.returnType = returnType;
    }


    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }


}