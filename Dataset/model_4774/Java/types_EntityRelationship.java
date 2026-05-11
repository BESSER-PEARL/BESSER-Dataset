





import java.util.List;
import java.util.ArrayList;

public class types_EntityRelationship  {

    private String kind;





    private types_Property types_property;


    public types_EntityRelationship(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public types_Property getTypes_property() {
        return types_property;
    }

    public void setTypes_property(types_Property types_property) {
        this.types_property = types_property;
    }

}