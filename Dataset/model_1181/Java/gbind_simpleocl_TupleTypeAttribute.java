





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_TupleTypeAttribute extends LocatedElement {

    private String name;





    private OclType ocltype;


    public gbind_simpleocl_TupleTypeAttribute(
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

    public OclType getOcltype() {
        return ocltype;
    }

    public void setOcltype(OclType ocltype) {
        this.ocltype = ocltype;
    }

}