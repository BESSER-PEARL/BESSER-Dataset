





import java.util.List;
import java.util.ArrayList;

public class ddsm_PeerToPeerPlatform extends InternalComponent {






    private List<ddsm_RequiredExecutionPlatform> ddsm_requiredexecutionplatforms;


    public ddsm_PeerToPeerPlatform(
    ) {
        super(
        );
        this.ddsm_requiredexecutionplatforms = new ArrayList<>();
    }

    public ddsm_PeerToPeerPlatform(
        ArrayList<ddsm_RequiredExecutionPlatform> ddsm_requiredexecutionplatforms    ) {
        this.ddsm_requiredexecutionplatforms = ddsm_requiredexecutionplatforms;
    }


    public List<ddsm_RequiredExecutionPlatform> getDdsm_requiredexecutionplatforms() {
        return ddsm_requiredexecutionplatforms;
    }

    public void addDdsm_requiredexecutionplatform(Ddsm_requiredexecutionplatform ddsm_requiredexecutionplatform) {
        this.ddsm_requiredexecutionplatforms.add(ddsm_requiredexecutionplatform);
    }

}