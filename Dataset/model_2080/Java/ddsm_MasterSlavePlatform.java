





import java.util.List;
import java.util.ArrayList;

public class ddsm_MasterSlavePlatform extends InternalComponent {






    private List<ddsm_RequiredExecutionPlatform> ddsm_requiredexecutionplatforms;




    private ddsm_RequiredExecutionPlatform ddsm_requiredexecutionplatform;


    public ddsm_MasterSlavePlatform(
    ) {
        super(
        );
        this.ddsm_requiredexecutionplatforms = new ArrayList<>();
    }

    public ddsm_MasterSlavePlatform(
        ArrayList<ddsm_RequiredExecutionPlatform> ddsm_requiredexecutionplatforms    ) {
        this.ddsm_requiredexecutionplatforms = ddsm_requiredexecutionplatforms;
    }


    public List<ddsm_RequiredExecutionPlatform> getDdsm_requiredexecutionplatforms() {
        return ddsm_requiredexecutionplatforms;
    }

    public void addDdsm_requiredexecutionplatform(Ddsm_requiredexecutionplatform ddsm_requiredexecutionplatform) {
        this.ddsm_requiredexecutionplatforms.add(ddsm_requiredexecutionplatform);
    }
    public ddsm_RequiredExecutionPlatform getDdsm_requiredexecutionplatform() {
        return ddsm_requiredexecutionplatform;
    }

    public void setDdsm_requiredexecutionplatform(ddsm_RequiredExecutionPlatform ddsm_requiredexecutionplatform) {
        this.ddsm_requiredexecutionplatform = ddsm_requiredexecutionplatform;
    }

}