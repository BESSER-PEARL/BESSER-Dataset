





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsPresentationQos  {

    private boolean coherent_access;
    private boolean ordered_access;
    private String access_scope;





    private ddsMetamodel_DdsSubscriberQosProfile ddsmetamodel_ddssubscriberqosprofile;




    private ddsMetamodel_DdsPublisherQosProfile ddsmetamodel_ddspublisherqosprofile;


    public ddsMetamodel_DdsPresentationQos(
        boolean coherent_access,        boolean ordered_access,        String access_scope    ) {
        this.coherent_access = coherent_access;
        this.ordered_access = ordered_access;
        this.access_scope = access_scope;
    }


    public boolean getCoherent_access() {
        return coherent_access;
    }

    public void setCoherent_access(boolean coherent_access) {
        this.coherent_access = coherent_access;
    }
    public boolean getOrdered_access() {
        return ordered_access;
    }

    public void setOrdered_access(boolean ordered_access) {
        this.ordered_access = ordered_access;
    }
    public String getAccess_scope() {
        return access_scope;
    }

    public void setAccess_scope(String access_scope) {
        this.access_scope = access_scope;
    }

    public ddsMetamodel_DdsSubscriberQosProfile getDdsmetamodel_ddssubscriberqosprofile() {
        return ddsmetamodel_ddssubscriberqosprofile;
    }

    public void setDdsmetamodel_ddssubscriberqosprofile(ddsMetamodel_DdsSubscriberQosProfile ddsmetamodel_ddssubscriberqosprofile) {
        this.ddsmetamodel_ddssubscriberqosprofile = ddsmetamodel_ddssubscriberqosprofile;
    }
    public ddsMetamodel_DdsPublisherQosProfile getDdsmetamodel_ddspublisherqosprofile() {
        return ddsmetamodel_ddspublisherqosprofile;
    }

    public void setDdsmetamodel_ddspublisherqosprofile(ddsMetamodel_DdsPublisherQosProfile ddsmetamodel_ddspublisherqosprofile) {
        this.ddsmetamodel_ddspublisherqosprofile = ddsmetamodel_ddspublisherqosprofile;
    }

}