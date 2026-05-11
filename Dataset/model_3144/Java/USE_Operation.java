





import java.util.List;
import java.util.ArrayList;

public class USE_Operation  {

    private String name;





    private USE_Class use_class;




    private List<USE_Parameter> use_parameters;


    public USE_Operation(
        String name    ) {
        this.name = name;
        this.use_parameters = new ArrayList<>();
    }

    public USE_Operation(
        String name        ArrayList<USE_Parameter> use_parameters    ) {
        this.name = name;
        this.use_parameters = use_parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public USE_Class getUse_class() {
        return use_class;
    }

    public void setUse_class(USE_Class use_class) {
        this.use_class = use_class;
    }
    public List<USE_Parameter> getUse_parameters() {
        return use_parameters;
    }

    public void addUse_parameter(Use_parameter use_parameter) {
        this.use_parameters.add(use_parameter);
    }

}