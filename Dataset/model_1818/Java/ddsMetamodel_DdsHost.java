





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsHost  {

    private String hostName;





    private List<ddsMetamodel_DdsApplication> ddsmetamodel_ddsapplications;




    private ddsMetamodel_DdsSystem ddsmetamodel_ddssystem;


    public ddsMetamodel_DdsHost(
        String hostName    ) {
        this.hostName = hostName;
        this.ddsmetamodel_ddsapplications = new ArrayList<>();
    }

    public ddsMetamodel_DdsHost(
        String hostName        ArrayList<ddsMetamodel_DdsApplication> ddsmetamodel_ddsapplications    ) {
        this.hostName = hostName;
        this.ddsmetamodel_ddsapplications = ddsmetamodel_ddsapplications;
    }

    public String getHostname() {
        return hostName;
    }

    public void setHostname(String hostName) {
        this.hostName = hostName;
    }

    public List<ddsMetamodel_DdsApplication> getDdsmetamodel_ddsapplications() {
        return ddsmetamodel_ddsapplications;
    }

    public void addDdsmetamodel_ddsapplication(Ddsmetamodel_ddsapplication ddsmetamodel_ddsapplication) {
        this.ddsmetamodel_ddsapplications.add(ddsmetamodel_ddsapplication);
    }
    public ddsMetamodel_DdsSystem getDdsmetamodel_ddssystem() {
        return ddsmetamodel_ddssystem;
    }

    public void setDdsmetamodel_ddssystem(ddsMetamodel_DdsSystem ddsmetamodel_ddssystem) {
        this.ddsmetamodel_ddssystem = ddsmetamodel_ddssystem;
    }

}