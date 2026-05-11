





import java.util.List;
import java.util.ArrayList;

public class archDSL_UncertainBehavior  {

    private String name;





    private archDSL_UncertainConnector archdsl_uncertainconnector;




    private archDSL_Interface archdsl_interface;




    private List<archDSL_SuperCall> archdsl_supercalls;


    public archDSL_UncertainBehavior(
        String name    ) {
        this.name = name;
        this.archdsl_supercalls = new ArrayList<>();
    }

    public archDSL_UncertainBehavior(
        String name        ArrayList<archDSL_SuperCall> archdsl_supercalls    ) {
        this.name = name;
        this.archdsl_supercalls = archdsl_supercalls;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public archDSL_UncertainConnector getArchdsl_uncertainconnector() {
        return archdsl_uncertainconnector;
    }

    public void setArchdsl_uncertainconnector(archDSL_UncertainConnector archdsl_uncertainconnector) {
        this.archdsl_uncertainconnector = archdsl_uncertainconnector;
    }
    public archDSL_Interface getArchdsl_interface() {
        return archdsl_interface;
    }

    public void setArchdsl_interface(archDSL_Interface archdsl_interface) {
        this.archdsl_interface = archdsl_interface;
    }
    public List<archDSL_SuperCall> getArchdsl_supercalls() {
        return archdsl_supercalls;
    }

    public void addArchdsl_supercall(Archdsl_supercall archdsl_supercall) {
        this.archdsl_supercalls.add(archdsl_supercall);
    }

}