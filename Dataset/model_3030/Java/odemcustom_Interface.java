





import java.util.List;
import java.util.ArrayList;

public class odemcustom_Interface extends Classifier {






    private odemcustom_Interface odemcustom_interface;




    private List<odemcustom_Procedure> odemcustom_procedures;




    private odemcustom_ClassSimilar odemcustom_classsimilar;


    public odemcustom_Interface(
    ) {
        super(
        );
        this.odemcustom_procedures = new ArrayList<>();
    }

    public odemcustom_Interface(
        ArrayList<odemcustom_Procedure> odemcustom_procedures    ) {
        this.odemcustom_procedures = odemcustom_procedures;
    }


    public odemcustom_Interface getOdemcustom_interface() {
        return odemcustom_interface;
    }

    public void setOdemcustom_interface(odemcustom_Interface odemcustom_interface) {
        this.odemcustom_interface = odemcustom_interface;
    }
    public List<odemcustom_Procedure> getOdemcustom_procedures() {
        return odemcustom_procedures;
    }

    public void addOdemcustom_procedure(Odemcustom_procedure odemcustom_procedure) {
        this.odemcustom_procedures.add(odemcustom_procedure);
    }
    public odemcustom_ClassSimilar getOdemcustom_classsimilar() {
        return odemcustom_classsimilar;
    }

    public void setOdemcustom_classsimilar(odemcustom_ClassSimilar odemcustom_classsimilar) {
        this.odemcustom_classsimilar = odemcustom_classsimilar;
    }

}