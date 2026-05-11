





import java.util.List;
import java.util.ArrayList;

public class ddsm_InternalComponent extends Component {






    private ddsm_InternalComponent ddsm_internalcomponent;




    private List<ddsm_RequiredExecutionPlatform> ddsm_requiredexecutionplatforms;


    public ddsm_InternalComponent(
    ) {
        super(
        );
        this.ddsm_requiredexecutionplatforms = new ArrayList<>();
    }

    public ddsm_InternalComponent(
        ArrayList<ddsm_RequiredExecutionPlatform> ddsm_requiredexecutionplatforms    ) {
        this.ddsm_requiredexecutionplatforms = ddsm_requiredexecutionplatforms;
    }


    public ddsm_InternalComponent getDdsm_internalcomponent() {
        return ddsm_internalcomponent;
    }

    public void setDdsm_internalcomponent(ddsm_InternalComponent ddsm_internalcomponent) {
        this.ddsm_internalcomponent = ddsm_internalcomponent;
    }
    public List<ddsm_RequiredExecutionPlatform> getDdsm_requiredexecutionplatforms() {
        return ddsm_requiredexecutionplatforms;
    }

    public void addDdsm_requiredexecutionplatform(Ddsm_requiredexecutionplatform ddsm_requiredexecutionplatform) {
        this.ddsm_requiredexecutionplatforms.add(ddsm_requiredexecutionplatform);
    }

}