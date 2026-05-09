





import java.util.List;
import java.util.ArrayList;

public class oCLlite_LambdaType extends OclLType {

    private String name;





    private List<oCLlite_OclLType> ocllite_oclltypes;




    private oCLlite_OclLType ocllite_oclltype;


    public oCLlite_LambdaType(
        String name    ) {
        super(
        );
        this.name = name;
        this.ocllite_oclltypes = new ArrayList<>();
    }

    public oCLlite_LambdaType(
        String name        ArrayList<oCLlite_OclLType> ocllite_oclltypes    ) {
        this.name = name;
        this.ocllite_oclltypes = ocllite_oclltypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<oCLlite_OclLType> getOcllite_oclltypes() {
        return ocllite_oclltypes;
    }

    public void addOcllite_oclltype(Ocllite_oclltype ocllite_oclltype) {
        this.ocllite_oclltypes.add(ocllite_oclltype);
    }
    public oCLlite_OclLType getOcllite_oclltype() {
        return ocllite_oclltype;
    }

    public void setOcllite_oclltype(oCLlite_OclLType ocllite_oclltype) {
        this.ocllite_oclltype = ocllite_oclltype;
    }

}