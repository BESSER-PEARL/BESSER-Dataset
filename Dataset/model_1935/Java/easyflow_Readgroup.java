





import java.util.List;
import java.util.ArrayList;

public class easyflow_Readgroup extends GroupingCriterion {

    private String platform;
    private String platformUnit;
    private String name;
    private String description;





    private easyflow_Record easyflow_record;


    public easyflow_Readgroup(
        String platform,        String platformUnit,        String name,        String description    ) {
        super(
        );
        this.platform = platform;
        this.platformUnit = platformUnit;
        this.name = name;
        this.description = description;
    }


    public String getPlatform() {
        return platform;
    }

    public void setPlatform(String platform) {
        this.platform = platform;
    }
    public String getPlatformunit() {
        return platformUnit;
    }

    public void setPlatformunit(String platformUnit) {
        this.platformUnit = platformUnit;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public easyflow_Record getEasyflow_record() {
        return easyflow_record;
    }

    public void setEasyflow_record(easyflow_Record easyflow_record) {
        this.easyflow_record = easyflow_record;
    }

}