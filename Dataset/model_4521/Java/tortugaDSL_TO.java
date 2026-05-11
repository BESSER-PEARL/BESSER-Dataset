





import java.util.List;
import java.util.ArrayList;

public class tortugaDSL_TO extends CONTROL_SENTENCES {

    private String name;





    private List<tortugaDSL_PARAM> tortugadsl_params;




    private tortugaDSL_PROCEDURE_CALL tortugadsl_procedure_call;


    public tortugaDSL_TO(
        String name    ) {
        super(
        );
        this.name = name;
        this.tortugadsl_params = new ArrayList<>();
    }

    public tortugaDSL_TO(
        String name        ArrayList<tortugaDSL_PARAM> tortugadsl_params    ) {
        this.name = name;
        this.tortugadsl_params = tortugadsl_params;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tortugaDSL_PARAM> getTortugadsl_params() {
        return tortugadsl_params;
    }

    public void addTortugadsl_param(Tortugadsl_param tortugadsl_param) {
        this.tortugadsl_params.add(tortugadsl_param);
    }
    public tortugaDSL_PROCEDURE_CALL getTortugadsl_procedure_call() {
        return tortugadsl_procedure_call;
    }

    public void setTortugadsl_procedure_call(tortugaDSL_PROCEDURE_CALL tortugadsl_procedure_call) {
        this.tortugadsl_procedure_call = tortugadsl_procedure_call;
    }

}