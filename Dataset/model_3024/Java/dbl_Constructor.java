





import java.util.List;
import java.util.ArrayList;

public class dbl_Constructor  {






    private List<dbl_Parameter> dbl_parameters;




    private dbl_Clazz dbl_clazz;


    public dbl_Constructor(
    ) {
        this.dbl_parameters = new ArrayList<>();
    }

    public dbl_Constructor(
        ArrayList<dbl_Parameter> dbl_parameters    ) {
        this.dbl_parameters = dbl_parameters;
    }


    public List<dbl_Parameter> getDbl_parameters() {
        return dbl_parameters;
    }

    public void addDbl_parameter(Dbl_parameter dbl_parameter) {
        this.dbl_parameters.add(dbl_parameter);
    }
    public dbl_Clazz getDbl_clazz() {
        return dbl_clazz;
    }

    public void setDbl_clazz(dbl_Clazz dbl_clazz) {
        this.dbl_clazz = dbl_clazz;
    }

}