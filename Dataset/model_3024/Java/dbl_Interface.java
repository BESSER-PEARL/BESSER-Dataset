





import java.util.List;
import java.util.ArrayList;

public class dbl_Interface extends Classifier {






    private dbl_ClassSimilar dbl_classsimilar;




    private List<dbl_Procedure> dbl_procedures;




    private dbl_Interface dbl_interface;


    public dbl_Interface(
    ) {
        super(
        );
        this.dbl_procedures = new ArrayList<>();
    }

    public dbl_Interface(
        ArrayList<dbl_Procedure> dbl_procedures    ) {
        this.dbl_procedures = dbl_procedures;
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
    public dbl_Interface getDbl_interface() {
        return dbl_interface;
    }

    public void setDbl_interface(dbl_Interface dbl_interface) {
        this.dbl_interface = dbl_interface;
    }

}