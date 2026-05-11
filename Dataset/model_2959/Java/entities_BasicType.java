





import java.util.List;
import java.util.ArrayList;

public class entities_BasicType extends ElementType {

    private String typeName;



    public entities_BasicType(
        String typeName    ) {
        super(
        );
        this.typeName = typeName;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }


}