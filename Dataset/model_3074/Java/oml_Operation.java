





import java.util.List;
import java.util.ArrayList;

public class oml_Operation extends Feature {






    private oml_Parameter oml_parameter;




    private List<oml_Parameter> oml_parameters;


    public oml_Operation(
    ) {
        super(
        );
        this.oml_parameters = new ArrayList<>();
    }

    public oml_Operation(
        ArrayList<oml_Parameter> oml_parameters    ) {
        this.oml_parameters = oml_parameters;
    }


    public oml_Parameter getOml_parameter() {
        return oml_parameter;
    }

    public void setOml_parameter(oml_Parameter oml_parameter) {
        this.oml_parameter = oml_parameter;
    }
    public List<oml_Parameter> getOml_parameters() {
        return oml_parameters;
    }

    public void addOml_parameter(Oml_parameter oml_parameter) {
        this.oml_parameters.add(oml_parameter);
    }

}