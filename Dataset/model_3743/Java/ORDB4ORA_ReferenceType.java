





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_ReferenceType extends Datatype {

    private String Name;





    private ORDB4ORA_StructuredType ordb4ora_structuredtype;


    public ORDB4ORA_ReferenceType(
        String Name    ) {
        super(
        );
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public ORDB4ORA_StructuredType getOrdb4ora_structuredtype() {
        return ordb4ora_structuredtype;
    }

    public void setOrdb4ora_structuredtype(ORDB4ORA_StructuredType ordb4ora_structuredtype) {
        this.ordb4ora_structuredtype = ordb4ora_structuredtype;
    }

}