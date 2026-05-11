





import java.util.List;
import java.util.ArrayList;

public class soopl_Method extends NamedElement {






    private List<soopl_Parameter> soopl_parameters;


    public soopl_Method(
    ) {
        super(
        );
        this.soopl_parameters = new ArrayList<>();
    }

    public soopl_Method(
        ArrayList<soopl_Parameter> soopl_parameters    ) {
        this.soopl_parameters = soopl_parameters;
    }


    public List<soopl_Parameter> getSoopl_parameters() {
        return soopl_parameters;
    }

    public void addSoopl_parameter(Soopl_parameter soopl_parameter) {
        this.soopl_parameters.add(soopl_parameter);
    }

}