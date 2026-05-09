





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsWaitSet  {

    private String name;





    private ddsMetamodel_DdsApplication ddsmetamodel_ddsapplication;


    public ddsMetamodel_DdsWaitSet(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ddsMetamodel_DdsApplication getDdsmetamodel_ddsapplication() {
        return ddsmetamodel_ddsapplication;
    }

    public void setDdsmetamodel_ddsapplication(ddsMetamodel_DdsApplication ddsmetamodel_ddsapplication) {
        this.ddsmetamodel_ddsapplication = ddsmetamodel_ddsapplication;
    }

}