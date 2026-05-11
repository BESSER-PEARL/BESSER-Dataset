





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlPrimitiveDataType extends SadlTypeReference {

    private String primitiveType;
    private boolean list;



    public sADL_SadlPrimitiveDataType(
        String primitiveType,        boolean list    ) {
        super(
        );
        this.primitiveType = primitiveType;
        this.list = list;
    }


    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }
    public boolean getList() {
        return list;
    }

    public void setList(boolean list) {
        this.list = list;
    }


}