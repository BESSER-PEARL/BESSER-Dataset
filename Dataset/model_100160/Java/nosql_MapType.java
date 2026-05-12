





import java.util.List;
import java.util.ArrayList;

public class nosql_MapType extends DataStructureType {

    private String keyType;
    private String baseType;



    public nosql_MapType(
        String keyType,        String baseType    ) {
        super(
        );
        this.keyType = keyType;
        this.baseType = baseType;
    }


    public String getKeytype() {
        return keyType;
    }

    public void setKeytype(String keyType) {
        this.keyType = keyType;
    }
    public String getBasetype() {
        return baseType;
    }

    public void setBasetype(String baseType) {
        this.baseType = baseType;
    }


}