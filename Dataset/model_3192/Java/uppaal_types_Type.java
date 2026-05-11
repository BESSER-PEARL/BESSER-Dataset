





import java.util.List;
import java.util.ArrayList;

public class uppaal_types_Type extends NamedElement {

    private String baseType;



    public uppaal_types_Type(
        String baseType    ) {
        super(
        );
        this.baseType = baseType;
    }


    public String getBasetype() {
        return baseType;
    }

    public void setBasetype(String baseType) {
        this.baseType = baseType;
    }


}