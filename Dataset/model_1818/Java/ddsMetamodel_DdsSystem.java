





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsSystem  {

    private String systemName;





    private List<ddsMetamodel_DdsQosProfile> ddsmetamodel_ddsqosprofiles;




    private ddsMetamodel_DdsDataModule ddsmetamodel_ddsdatamodule;




    private List<ddsMetamodel_DdsTopic> ddsmetamodel_ddstopics;




    private List<ddsMetamodel_DdsDataModule> ddsmetamodel_ddsdatamodules;


    public ddsMetamodel_DdsSystem(
        String systemName    ) {
        this.systemName = systemName;
        this.ddsmetamodel_ddsqosprofiles = new ArrayList<>();
        this.ddsmetamodel_ddstopics = new ArrayList<>();
        this.ddsmetamodel_ddsdatamodules = new ArrayList<>();
    }

    public ddsMetamodel_DdsSystem(
        String systemName        ArrayList<ddsMetamodel_DdsQosProfile> ddsmetamodel_ddsqosprofiles,        ArrayList<ddsMetamodel_DdsTopic> ddsmetamodel_ddstopics,        ArrayList<ddsMetamodel_DdsDataModule> ddsmetamodel_ddsdatamodules    ) {
        this.systemName = systemName;
        this.ddsmetamodel_ddsqosprofiles = ddsmetamodel_ddsqosprofiles;
        this.ddsmetamodel_ddstopics = ddsmetamodel_ddstopics;
        this.ddsmetamodel_ddsdatamodules = ddsmetamodel_ddsdatamodules;
    }

    public String getSystemname() {
        return systemName;
    }

    public void setSystemname(String systemName) {
        this.systemName = systemName;
    }

    public List<ddsMetamodel_DdsQosProfile> getDdsmetamodel_ddsqosprofiles() {
        return ddsmetamodel_ddsqosprofiles;
    }

    public void addDdsmetamodel_ddsqosprofile(Ddsmetamodel_ddsqosprofile ddsmetamodel_ddsqosprofile) {
        this.ddsmetamodel_ddsqosprofiles.add(ddsmetamodel_ddsqosprofile);
    }
    public ddsMetamodel_DdsDataModule getDdsmetamodel_ddsdatamodule() {
        return ddsmetamodel_ddsdatamodule;
    }

    public void setDdsmetamodel_ddsdatamodule(ddsMetamodel_DdsDataModule ddsmetamodel_ddsdatamodule) {
        this.ddsmetamodel_ddsdatamodule = ddsmetamodel_ddsdatamodule;
    }
    public List<ddsMetamodel_DdsTopic> getDdsmetamodel_ddstopics() {
        return ddsmetamodel_ddstopics;
    }

    public void addDdsmetamodel_ddstopic(Ddsmetamodel_ddstopic ddsmetamodel_ddstopic) {
        this.ddsmetamodel_ddstopics.add(ddsmetamodel_ddstopic);
    }
    public List<ddsMetamodel_DdsDataModule> getDdsmetamodel_ddsdatamodules() {
        return ddsmetamodel_ddsdatamodules;
    }

    public void addDdsmetamodel_ddsdatamodule(Ddsmetamodel_ddsdatamodule ddsmetamodel_ddsdatamodule) {
        this.ddsmetamodel_ddsdatamodules.add(ddsmetamodel_ddsdatamodule);
    }

}