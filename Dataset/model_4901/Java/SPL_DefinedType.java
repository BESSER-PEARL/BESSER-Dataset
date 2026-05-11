





import java.util.List;
import java.util.ArrayList;

public class SPL_DefinedType extends TypeExpression {

    private String typeName;



    public SPL_DefinedType(
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