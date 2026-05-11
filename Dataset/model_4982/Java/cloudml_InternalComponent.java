





import java.util.List;
import java.util.ArrayList;

public class cloudml_InternalComponent extends Component {






    private cloudml_CloudMLModel cloudml_cloudmlmodel;




    private List<cloudml_InternalComponent> cloudml_internalcomponents;


    public cloudml_InternalComponent(
    ) {
        super(
        );
        this.cloudml_internalcomponents = new ArrayList<>();
    }

    public cloudml_InternalComponent(
        ArrayList<cloudml_InternalComponent> cloudml_internalcomponents    ) {
        this.cloudml_internalcomponents = cloudml_internalcomponents;
    }


    public cloudml_CloudMLModel getCloudml_cloudmlmodel() {
        return cloudml_cloudmlmodel;
    }

    public void setCloudml_cloudmlmodel(cloudml_CloudMLModel cloudml_cloudmlmodel) {
        this.cloudml_cloudmlmodel = cloudml_cloudmlmodel;
    }
    public List<cloudml_InternalComponent> getCloudml_internalcomponents() {
        return cloudml_internalcomponents;
    }

    public void addCloudml_internalcomponent(Cloudml_internalcomponent cloudml_internalcomponent) {
        this.cloudml_internalcomponents.add(cloudml_internalcomponent);
    }

}