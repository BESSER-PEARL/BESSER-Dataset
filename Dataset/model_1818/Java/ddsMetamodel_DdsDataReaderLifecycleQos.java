





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDataReaderLifecycleQos  {

    private boolean autopurge_dispose_all;
    private boolean enable_invalid_samples;





    private ddsMetamodel_DdsDuration ddsmetamodel_ddsduration;




    private ddsMetamodel_DdsDuration ddsmetamodel_ddsduration;




    private ddsMetamodel_DdsDataReaderQosProfile ddsmetamodel_ddsdatareaderqosprofile;


    public ddsMetamodel_DdsDataReaderLifecycleQos(
        boolean autopurge_dispose_all,        boolean enable_invalid_samples    ) {
        this.autopurge_dispose_all = autopurge_dispose_all;
        this.enable_invalid_samples = enable_invalid_samples;
    }


    public boolean getAutopurge_dispose_all() {
        return autopurge_dispose_all;
    }

    public void setAutopurge_dispose_all(boolean autopurge_dispose_all) {
        this.autopurge_dispose_all = autopurge_dispose_all;
    }
    public boolean getEnable_invalid_samples() {
        return enable_invalid_samples;
    }

    public void setEnable_invalid_samples(boolean enable_invalid_samples) {
        this.enable_invalid_samples = enable_invalid_samples;
    }

    public ddsMetamodel_DdsDuration getDdsmetamodel_ddsduration() {
        return ddsmetamodel_ddsduration;
    }

    public void setDdsmetamodel_ddsduration(ddsMetamodel_DdsDuration ddsmetamodel_ddsduration) {
        this.ddsmetamodel_ddsduration = ddsmetamodel_ddsduration;
    }
    public ddsMetamodel_DdsDuration getDdsmetamodel_ddsduration() {
        return ddsmetamodel_ddsduration;
    }

    public void setDdsmetamodel_ddsduration(ddsMetamodel_DdsDuration ddsmetamodel_ddsduration) {
        this.ddsmetamodel_ddsduration = ddsmetamodel_ddsduration;
    }
    public ddsMetamodel_DdsDataReaderQosProfile getDdsmetamodel_ddsdatareaderqosprofile() {
        return ddsmetamodel_ddsdatareaderqosprofile;
    }

    public void setDdsmetamodel_ddsdatareaderqosprofile(ddsMetamodel_DdsDataReaderQosProfile ddsmetamodel_ddsdatareaderqosprofile) {
        this.ddsmetamodel_ddsdatareaderqosprofile = ddsmetamodel_ddsdatareaderqosprofile;
    }

}