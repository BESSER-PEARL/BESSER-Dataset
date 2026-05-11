





import java.util.List;
import java.util.ArrayList;

public class camel_deployment_InternalComponent extends Component {

    private String version;





    private List<InternalComponent> internalcomponents;


    public camel_deployment_InternalComponent(
        String version    ) {
        super(
        );
        this.version = version;
        this.internalcomponents = new ArrayList<>();
    }

    public camel_deployment_InternalComponent(
        String version        ArrayList<InternalComponent> internalcomponents    ) {
        this.version = version;
        this.internalcomponents = internalcomponents;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public List<InternalComponent> getInternalcomponents() {
        return internalcomponents;
    }

    public void addInternalcomponent(Internalcomponent internalcomponent) {
        this.internalcomponents.add(internalcomponent);
    }

}