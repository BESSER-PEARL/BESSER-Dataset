





import java.util.List;
import java.util.ArrayList;

public class easyflow_Readgroup extends GroupingCriterion {

    private String description;
    private String platform;
    private String name;
    private String platformUnit;





    private easyflow_StringToReadgroupMap easyflow_stringtoreadgroupmap;




    private List<easyflow_StringToLibraryMap> easyflow_stringtolibrarymaps;




    private List<easyflow_StringToSampleMap> easyflow_stringtosamplemaps;


    public easyflow_Readgroup(
        String description,        String platform,        String name,        String platformUnit    ) {
        super(
        );
        this.description = description;
        this.platform = platform;
        this.name = name;
        this.platformUnit = platformUnit;
        this.easyflow_stringtolibrarymaps = new ArrayList<>();
        this.easyflow_stringtosamplemaps = new ArrayList<>();
    }

    public easyflow_Readgroup(
        String description,        String platform,        String name,        String platformUnit        ArrayList<easyflow_StringToLibraryMap> easyflow_stringtolibrarymaps,        ArrayList<easyflow_StringToSampleMap> easyflow_stringtosamplemaps    ) {
        this.description = description;
        this.platform = platform;
        this.name = name;
        this.platformUnit = platformUnit;
        this.easyflow_stringtolibrarymaps = easyflow_stringtolibrarymaps;
        this.easyflow_stringtosamplemaps = easyflow_stringtosamplemaps;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPlatform() {
        return platform;
    }

    public void setPlatform(String platform) {
        this.platform = platform;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPlatformunit() {
        return platformUnit;
    }

    public void setPlatformunit(String platformUnit) {
        this.platformUnit = platformUnit;
    }

    public easyflow_StringToReadgroupMap getEasyflow_stringtoreadgroupmap() {
        return easyflow_stringtoreadgroupmap;
    }

    public void setEasyflow_stringtoreadgroupmap(easyflow_StringToReadgroupMap easyflow_stringtoreadgroupmap) {
        this.easyflow_stringtoreadgroupmap = easyflow_stringtoreadgroupmap;
    }
    public List<easyflow_StringToLibraryMap> getEasyflow_stringtolibrarymaps() {
        return easyflow_stringtolibrarymaps;
    }

    public void addEasyflow_stringtolibrarymap(Easyflow_stringtolibrarymap easyflow_stringtolibrarymap) {
        this.easyflow_stringtolibrarymaps.add(easyflow_stringtolibrarymap);
    }
    public List<easyflow_StringToSampleMap> getEasyflow_stringtosamplemaps() {
        return easyflow_stringtosamplemaps;
    }

    public void addEasyflow_stringtosamplemap(Easyflow_stringtosamplemap easyflow_stringtosamplemap) {
        this.easyflow_stringtosamplemaps.add(easyflow_stringtosamplemap);
    }

}