





import java.util.List;
import java.util.ArrayList;

public class OCL_TupleTypeAttribute extends LocatedElement {

    private String name;





    private TupleType tupletype;


    public OCL_TupleTypeAttribute(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public TupleType getTupletype() {
        return tupletype;
    }

    public void setTupletype(TupleType tupletype) {
        this.tupletype = tupletype;
    }

}