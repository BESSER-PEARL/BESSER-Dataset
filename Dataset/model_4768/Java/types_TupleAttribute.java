





import java.util.List;
import java.util.ArrayList;

public class types_TupleAttribute  {

    private String name;





    private types_TupleType types_tupletype;


    public types_TupleAttribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public types_TupleType getTypes_tupletype() {
        return types_tupletype;
    }

    public void setTypes_tupletype(types_TupleType types_tupletype) {
        this.types_tupletype = types_tupletype;
    }

}