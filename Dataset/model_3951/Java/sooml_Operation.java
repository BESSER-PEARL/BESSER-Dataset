





import java.util.List;
import java.util.ArrayList;

public class sooml_Operation extends NamedElement {






    private sooml_Class sooml_class;




    private List<sooml_Parameter> sooml_parameters;


    public sooml_Operation(
    ) {
        super(
        );
        this.sooml_parameters = new ArrayList<>();
    }

    public sooml_Operation(
        ArrayList<sooml_Parameter> sooml_parameters    ) {
        this.sooml_parameters = sooml_parameters;
    }


    public sooml_Class getSooml_class() {
        return sooml_class;
    }

    public void setSooml_class(sooml_Class sooml_class) {
        this.sooml_class = sooml_class;
    }
    public List<sooml_Parameter> getSooml_parameters() {
        return sooml_parameters;
    }

    public void addSooml_parameter(Sooml_parameter sooml_parameter) {
        this.sooml_parameters.add(sooml_parameter);
    }

}