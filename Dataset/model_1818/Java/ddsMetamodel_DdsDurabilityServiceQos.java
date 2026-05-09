





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDurabilityServiceQos  {

    private String history_depth;
    private String max_samples;
    private String max_instances;
    private String history_kind;
    private String max_samples_per_instances;





    private ddsMetamodel_DdsTopicQosProfile ddsmetamodel_ddstopicqosprofile;


    public ddsMetamodel_DdsDurabilityServiceQos(
        String history_depth,        String max_samples,        String max_instances,        String history_kind,        String max_samples_per_instances    ) {
        this.history_depth = history_depth;
        this.max_samples = max_samples;
        this.max_instances = max_instances;
        this.history_kind = history_kind;
        this.max_samples_per_instances = max_samples_per_instances;
    }


    public String getHistory_depth() {
        return history_depth;
    }

    public void setHistory_depth(String history_depth) {
        this.history_depth = history_depth;
    }
    public String getMax_samples() {
        return max_samples;
    }

    public void setMax_samples(String max_samples) {
        this.max_samples = max_samples;
    }
    public String getMax_instances() {
        return max_instances;
    }

    public void setMax_instances(String max_instances) {
        this.max_instances = max_instances;
    }
    public String getHistory_kind() {
        return history_kind;
    }

    public void setHistory_kind(String history_kind) {
        this.history_kind = history_kind;
    }
    public String getMax_samples_per_instances() {
        return max_samples_per_instances;
    }

    public void setMax_samples_per_instances(String max_samples_per_instances) {
        this.max_samples_per_instances = max_samples_per_instances;
    }

    public ddsMetamodel_DdsTopicQosProfile getDdsmetamodel_ddstopicqosprofile() {
        return ddsmetamodel_ddstopicqosprofile;
    }

    public void setDdsmetamodel_ddstopicqosprofile(ddsMetamodel_DdsTopicQosProfile ddsmetamodel_ddstopicqosprofile) {
        this.ddsmetamodel_ddstopicqosprofile = ddsmetamodel_ddstopicqosprofile;
    }

}