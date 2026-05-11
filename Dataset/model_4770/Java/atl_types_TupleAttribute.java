





import java.util.List;
import java.util.ArrayList;

public class atl_types_TupleAttribute  {

    private String name;





    private atl_types_Type atl_types_type;




    private atl_types_TupleType atl_types_tupletype;


    public atl_types_TupleAttribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public atl_types_Type getAtl_types_type() {
        return atl_types_type;
    }

    public void setAtl_types_type(atl_types_Type atl_types_type) {
        this.atl_types_type = atl_types_type;
    }
    public atl_types_TupleType getAtl_types_tupletype() {
        return atl_types_tupletype;
    }

    public void setAtl_types_tupletype(atl_types_TupleType atl_types_tupletype) {
        this.atl_types_tupletype = atl_types_tupletype;
    }

}