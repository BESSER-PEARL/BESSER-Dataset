





import java.util.List;
import java.util.ArrayList;

public class aDSL_Operator extends Member {

    private String opName;





    private List<aDSL_Parameter> adsl_parameters;


    public aDSL_Operator(
        String opName    ) {
        super(
        );
        this.opName = opName;
        this.adsl_parameters = new ArrayList<>();
    }

    public aDSL_Operator(
        String opName        ArrayList<aDSL_Parameter> adsl_parameters    ) {
        this.opName = opName;
        this.adsl_parameters = adsl_parameters;
    }

    public String getOpname() {
        return opName;
    }

    public void setOpname(String opName) {
        this.opName = opName;
    }

    public List<aDSL_Parameter> getAdsl_parameters() {
        return adsl_parameters;
    }

    public void addAdsl_parameter(Adsl_parameter adsl_parameter) {
        this.adsl_parameters.add(adsl_parameter);
    }

}