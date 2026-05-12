





import java.util.List;
import java.util.ArrayList;

public class dbca_Function extends DatabaseElement {

    private String returnType;



    public dbca_Function(
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