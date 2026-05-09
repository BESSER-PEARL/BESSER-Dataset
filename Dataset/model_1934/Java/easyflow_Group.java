





import java.util.List;
import java.util.ArrayList;

public class easyflow_Group extends GroupingCriterion {

    private String name;





    private easyflow_StringToGroupMap easyflow_stringtogroupmap;




    private List<easyflow_StringToLibraryMap> easyflow_stringtolibrarymaps;




    private List<easyflow_StringToRecordMap> easyflow_stringtorecordmaps;




    private List<easyflow_StringToSampleMap> easyflow_stringtosamplemaps;




    private List<easyflow_StringToReadgroupMap> easyflow_stringtoreadgroupmaps;


    public easyflow_Group(
        String name    ) {
        super(
        );
        this.name = name;
        this.easyflow_stringtolibrarymaps = new ArrayList<>();
        this.easyflow_stringtorecordmaps = new ArrayList<>();
        this.easyflow_stringtosamplemaps = new ArrayList<>();
        this.easyflow_stringtoreadgroupmaps = new ArrayList<>();
    }

    public easyflow_Group(
        String name        ArrayList<easyflow_StringToLibraryMap> easyflow_stringtolibrarymaps,        ArrayList<easyflow_StringToRecordMap> easyflow_stringtorecordmaps,        ArrayList<easyflow_StringToSampleMap> easyflow_stringtosamplemaps,        ArrayList<easyflow_StringToReadgroupMap> easyflow_stringtoreadgroupmaps    ) {
        this.name = name;
        this.easyflow_stringtolibrarymaps = easyflow_stringtolibrarymaps;
        this.easyflow_stringtorecordmaps = easyflow_stringtorecordmaps;
        this.easyflow_stringtosamplemaps = easyflow_stringtosamplemaps;
        this.easyflow_stringtoreadgroupmaps = easyflow_stringtoreadgroupmaps;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public easyflow_StringToGroupMap getEasyflow_stringtogroupmap() {
        return easyflow_stringtogroupmap;
    }

    public void setEasyflow_stringtogroupmap(easyflow_StringToGroupMap easyflow_stringtogroupmap) {
        this.easyflow_stringtogroupmap = easyflow_stringtogroupmap;
    }
    public List<easyflow_StringToLibraryMap> getEasyflow_stringtolibrarymaps() {
        return easyflow_stringtolibrarymaps;
    }

    public void addEasyflow_stringtolibrarymap(Easyflow_stringtolibrarymap easyflow_stringtolibrarymap) {
        this.easyflow_stringtolibrarymaps.add(easyflow_stringtolibrarymap);
    }
    public List<easyflow_StringToRecordMap> getEasyflow_stringtorecordmaps() {
        return easyflow_stringtorecordmaps;
    }

    public void addEasyflow_stringtorecordmap(Easyflow_stringtorecordmap easyflow_stringtorecordmap) {
        this.easyflow_stringtorecordmaps.add(easyflow_stringtorecordmap);
    }
    public List<easyflow_StringToSampleMap> getEasyflow_stringtosamplemaps() {
        return easyflow_stringtosamplemaps;
    }

    public void addEasyflow_stringtosamplemap(Easyflow_stringtosamplemap easyflow_stringtosamplemap) {
        this.easyflow_stringtosamplemaps.add(easyflow_stringtosamplemap);
    }
    public List<easyflow_StringToReadgroupMap> getEasyflow_stringtoreadgroupmaps() {
        return easyflow_stringtoreadgroupmaps;
    }

    public void addEasyflow_stringtoreadgroupmap(Easyflow_stringtoreadgroupmap easyflow_stringtoreadgroupmap) {
        this.easyflow_stringtoreadgroupmaps.add(easyflow_stringtoreadgroupmap);
    }

}