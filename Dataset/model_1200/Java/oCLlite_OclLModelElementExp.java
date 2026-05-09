





import java.util.List;
import java.util.ArrayList;

public class oCLlite_OclLModelElementExp extends OclLType {

    private String name;





    private oCLlite_OclLModel ocllite_ocllmodel;


    public oCLlite_OclLModelElementExp(
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

    public oCLlite_OclLModel getOcllite_ocllmodel() {
        return ocllite_ocllmodel;
    }

    public void setOcllite_ocllmodel(oCLlite_OclLModel ocllite_ocllmodel) {
        this.ocllite_ocllmodel = ocllite_ocllmodel;
    }

}