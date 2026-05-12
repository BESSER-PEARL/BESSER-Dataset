





import java.util.List;
import java.util.ArrayList;

public class nosql_CollectionType extends DataStructureType {

    private String kind;
    private String keyType;



    public nosql_CollectionType(
        String kind,        String keyType    ) {
        super(
        );
        this.kind = kind;
        this.keyType = keyType;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getKeytype() {
        return keyType;
    }

    public void setKeytype(String keyType) {
        this.keyType = keyType;
    }


}