





import java.util.List;
import java.util.ArrayList;

public class odemcustom_Constructor  {






    private odemcustom_Clazz odemcustom_clazz;




    private List<odemcustom_Parameter> odemcustom_parameters;


    public odemcustom_Constructor(
    ) {
        this.odemcustom_parameters = new ArrayList<>();
    }

    public odemcustom_Constructor(
        ArrayList<odemcustom_Parameter> odemcustom_parameters    ) {
        this.odemcustom_parameters = odemcustom_parameters;
    }


    public odemcustom_Clazz getOdemcustom_clazz() {
        return odemcustom_clazz;
    }

    public void setOdemcustom_clazz(odemcustom_Clazz odemcustom_clazz) {
        this.odemcustom_clazz = odemcustom_clazz;
    }
    public List<odemcustom_Parameter> getOdemcustom_parameters() {
        return odemcustom_parameters;
    }

    public void addOdemcustom_parameter(Odemcustom_parameter odemcustom_parameter) {
        this.odemcustom_parameters.add(odemcustom_parameter);
    }

}