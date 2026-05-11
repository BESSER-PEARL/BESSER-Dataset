





import java.util.List;
import java.util.ArrayList;

public class qualitymodel_Metric  {

    private String resourceName;
    private String descriptionName;
    private String data;
    private String probeName;



    public qualitymodel_Metric(
        String resourceName,        String descriptionName,        String data,        String probeName    ) {
        this.resourceName = resourceName;
        this.descriptionName = descriptionName;
        this.data = data;
        this.probeName = probeName;
    }


    public String getResourcename() {
        return resourceName;
    }

    public void setResourcename(String resourceName) {
        this.resourceName = resourceName;
    }
    public String getDescriptionname() {
        return descriptionName;
    }

    public void setDescriptionname(String descriptionName) {
        this.descriptionName = descriptionName;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getProbename() {
        return probeName;
    }

    public void setProbename(String probeName) {
        this.probeName = probeName;
    }


}