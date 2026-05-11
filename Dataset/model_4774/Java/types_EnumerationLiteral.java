





import java.util.List;
import java.util.ArrayList;

public class types_EnumerationLiteral  {

    private String name;





    private types_EnumerationType types_enumerationtype;


    public types_EnumerationLiteral(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public types_EnumerationType getTypes_enumerationtype() {
        return types_enumerationtype;
    }

    public void setTypes_enumerationtype(types_EnumerationType types_enumerationtype) {
        this.types_enumerationtype = types_enumerationtype;
    }

}