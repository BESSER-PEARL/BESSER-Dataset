





import java.util.List;
import java.util.ArrayList;

public class oCLlite_SetType extends OclLType {

    private String name;





    private oCLlite_OclLType ocllite_oclltype;


    public oCLlite_SetType(
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

    public oCLlite_OclLType getOcllite_oclltype() {
        return ocllite_oclltype;
    }

    public void setOcllite_oclltype(oCLlite_OclLType ocllite_oclltype) {
        this.ocllite_oclltype = ocllite_oclltype;
    }

}