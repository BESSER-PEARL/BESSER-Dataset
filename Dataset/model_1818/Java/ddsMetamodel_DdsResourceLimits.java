





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsResourceLimits  {

    private String max_samples_per_instances;
    private String max_instances;
    private String max_samples;





    private ddsMetamodel_DdsDataReaderQosProfile ddsmetamodel_ddsdatareaderqosprofile;




    private ddsMetamodel_DdsDataWriterQosProfile ddsmetamodel_ddsdatawriterqosprofile;




    private ddsMetamodel_DdsTopicQosProfile ddsmetamodel_ddstopicqosprofile;


    public ddsMetamodel_DdsResourceLimits(
        String max_samples_per_instances,        String max_instances,        String max_samples    ) {
        this.max_samples_per_instances = max_samples_per_instances;
        this.max_instances = max_instances;
        this.max_samples = max_samples;
    }


    public String getMax_samples_per_instances() {
        return max_samples_per_instances;
    }

    public void setMax_samples_per_instances(String max_samples_per_instances) {
        this.max_samples_per_instances = max_samples_per_instances;
    }
    public String getMax_instances() {
        return max_instances;
    }

    public void setMax_instances(String max_instances) {
        this.max_instances = max_instances;
    }
    public String getMax_samples() {
        return max_samples;
    }

    public void setMax_samples(String max_samples) {
        this.max_samples = max_samples;
    }

    public ddsMetamodel_DdsDataReaderQosProfile getDdsmetamodel_ddsdatareaderqosprofile() {
        return ddsmetamodel_ddsdatareaderqosprofile;
    }

    public void setDdsmetamodel_ddsdatareaderqosprofile(ddsMetamodel_DdsDataReaderQosProfile ddsmetamodel_ddsdatareaderqosprofile) {
        this.ddsmetamodel_ddsdatareaderqosprofile = ddsmetamodel_ddsdatareaderqosprofile;
    }
    public ddsMetamodel_DdsDataWriterQosProfile getDdsmetamodel_ddsdatawriterqosprofile() {
        return ddsmetamodel_ddsdatawriterqosprofile;
    }

    public void setDdsmetamodel_ddsdatawriterqosprofile(ddsMetamodel_DdsDataWriterQosProfile ddsmetamodel_ddsdatawriterqosprofile) {
        this.ddsmetamodel_ddsdatawriterqosprofile = ddsmetamodel_ddsdatawriterqosprofile;
    }
    public ddsMetamodel_DdsTopicQosProfile getDdsmetamodel_ddstopicqosprofile() {
        return ddsmetamodel_ddstopicqosprofile;
    }

    public void setDdsmetamodel_ddstopicqosprofile(ddsMetamodel_DdsTopicQosProfile ddsmetamodel_ddstopicqosprofile) {
        this.ddsmetamodel_ddstopicqosprofile = ddsmetamodel_ddstopicqosprofile;
    }

}