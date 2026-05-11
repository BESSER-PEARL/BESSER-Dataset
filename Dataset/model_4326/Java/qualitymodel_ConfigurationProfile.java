





import java.util.List;
import java.util.ArrayList;

public class qualitymodel_ConfigurationProfile  {

    private int ID;





    private List<qualitymodel_Preference> qualitymodel_preferences;




    private List<qualitymodel_Metric> qualitymodel_metrics;


    public qualitymodel_ConfigurationProfile(
        int ID    ) {
        this.ID = ID;
        this.qualitymodel_preferences = new ArrayList<>();
        this.qualitymodel_metrics = new ArrayList<>();
    }

    public qualitymodel_ConfigurationProfile(
        int ID        ArrayList<qualitymodel_Preference> qualitymodel_preferences,        ArrayList<qualitymodel_Metric> qualitymodel_metrics    ) {
        this.ID = ID;
        this.qualitymodel_preferences = qualitymodel_preferences;
        this.qualitymodel_metrics = qualitymodel_metrics;
    }

    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public List<qualitymodel_Preference> getQualitymodel_preferences() {
        return qualitymodel_preferences;
    }

    public void addQualitymodel_preference(Qualitymodel_preference qualitymodel_preference) {
        this.qualitymodel_preferences.add(qualitymodel_preference);
    }
    public List<qualitymodel_Metric> getQualitymodel_metrics() {
        return qualitymodel_metrics;
    }

    public void addQualitymodel_metric(Qualitymodel_metric qualitymodel_metric) {
        this.qualitymodel_metrics.add(qualitymodel_metric);
    }

}