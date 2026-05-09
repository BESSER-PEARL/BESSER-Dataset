





import java.util.List;
import java.util.ArrayList;

public class easyflow_Sample extends GroupingCriterion {

    private String name;





    private easyflow_StringToSampleMap easyflow_stringtosamplemap;




    private List<easyflow_StringToRecordMap> easyflow_stringtorecordmaps;




    private List<easyflow_StringToReadgroupMap> easyflow_stringtoreadgroupmaps;




    private List<easyflow_StringToLibraryMap> easyflow_stringtolibrarymaps;


    public easyflow_Sample(
        String name    ) {
        super(
        );
        this.name = name;
        this.easyflow_stringtorecordmaps = new ArrayList<>();
        this.easyflow_stringtoreadgroupmaps = new ArrayList<>();
        this.easyflow_stringtolibrarymaps = new ArrayList<>();
    }

    public easyflow_Sample(
        String name        ArrayList<easyflow_StringToRecordMap> easyflow_stringtorecordmaps,        ArrayList<easyflow_StringToReadgroupMap> easyflow_stringtoreadgroupmaps,        ArrayList<easyflow_StringToLibraryMap> easyflow_stringtolibrarymaps    ) {
        this.name = name;
        this.easyflow_stringtorecordmaps = easyflow_stringtorecordmaps;
        this.easyflow_stringtoreadgroupmaps = easyflow_stringtoreadgroupmaps;
        this.easyflow_stringtolibrarymaps = easyflow_stringtolibrarymaps;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public easyflow_StringToSampleMap getEasyflow_stringtosamplemap() {
        return easyflow_stringtosamplemap;
    }

    public void setEasyflow_stringtosamplemap(easyflow_StringToSampleMap easyflow_stringtosamplemap) {
        this.easyflow_stringtosamplemap = easyflow_stringtosamplemap;
    }
    public List<easyflow_StringToRecordMap> getEasyflow_stringtorecordmaps() {
        return easyflow_stringtorecordmaps;
    }

    public void addEasyflow_stringtorecordmap(Easyflow_stringtorecordmap easyflow_stringtorecordmap) {
        this.easyflow_stringtorecordmaps.add(easyflow_stringtorecordmap);
    }
    public List<easyflow_StringToReadgroupMap> getEasyflow_stringtoreadgroupmaps() {
        return easyflow_stringtoreadgroupmaps;
    }

    public void addEasyflow_stringtoreadgroupmap(Easyflow_stringtoreadgroupmap easyflow_stringtoreadgroupmap) {
        this.easyflow_stringtoreadgroupmaps.add(easyflow_stringtoreadgroupmap);
    }
    public List<easyflow_StringToLibraryMap> getEasyflow_stringtolibrarymaps() {
        return easyflow_stringtolibrarymaps;
    }

    public void addEasyflow_stringtolibrarymap(Easyflow_stringtolibrarymap easyflow_stringtolibrarymap) {
        this.easyflow_stringtolibrarymaps.add(easyflow_stringtolibrarymap);
    }

}