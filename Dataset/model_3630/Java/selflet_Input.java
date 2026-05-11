





import java.util.List;
import java.util.ArrayList;

public class selflet_Input  {






    private List<selflet_Parameter> selflet_parameters;




    private selflet_Service selflet_service;


    public selflet_Input(
    ) {
        this.selflet_parameters = new ArrayList<>();
    }

    public selflet_Input(
        ArrayList<selflet_Parameter> selflet_parameters    ) {
        this.selflet_parameters = selflet_parameters;
    }


    public List<selflet_Parameter> getSelflet_parameters() {
        return selflet_parameters;
    }

    public void addSelflet_parameter(Selflet_parameter selflet_parameter) {
        this.selflet_parameters.add(selflet_parameter);
    }
    public selflet_Service getSelflet_service() {
        return selflet_service;
    }

    public void setSelflet_service(selflet_Service selflet_service) {
        this.selflet_service = selflet_service;
    }

}