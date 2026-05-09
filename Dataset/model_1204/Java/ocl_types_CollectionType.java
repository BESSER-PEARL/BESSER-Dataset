





import java.util.List;
import java.util.ArrayList;

public class ocl_types_CollectionType extends EDataType, utilities_PredefinedType, utilities_TypedASTNode {

    private String kind;



    public ocl_types_CollectionType(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}