





import java.util.List;
import java.util.ArrayList;

public class dbl_Interface extends Classifier {






    private List<dbl_Interface> dbl_interfaces;




    private dbl_ClassSimilar dbl_classsimilar;




    private List<dbl_Procedure> dbl_procedures;


    public dbl_Interface(
    ) {
        super(
        );
        this.dbl_interfaces = new ArrayList<>();
        this.dbl_procedures = new ArrayList<>();
    }

    public dbl_Interface(
        ArrayList<dbl_Interface> dbl_interfaces,        ArrayList<dbl_Procedure> dbl_procedures    ) {
        this.dbl_interfaces = dbl_interfaces;
        this.dbl_procedures = dbl_procedures;
    }


    public List<dbl_Interface> getDbl_interfaces() {
        return dbl_interfaces;
    }

    public void addDbl_interface(Dbl_interface dbl_interface) {
        this.dbl_interfaces.add(dbl_interface);
    }
    public dbl_ClassSimilar getDbl_classsimilar() {
        return dbl_classsimilar;
    }

    public void setDbl_classsimilar(dbl_ClassSimilar dbl_classsimilar) {
        this.dbl_classsimilar = dbl_classsimilar;
    }
    public List<dbl_Procedure> getDbl_procedures() {
        return dbl_procedures;
    }

    public void addDbl_procedure(Dbl_procedure dbl_procedure) {
        this.dbl_procedures.add(dbl_procedure);
    }

}