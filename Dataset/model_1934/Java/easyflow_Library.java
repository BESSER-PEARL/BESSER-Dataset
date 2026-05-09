





import java.util.List;
import java.util.ArrayList;

public class easyflow_Library extends GroupingCriterion {

    private String name;
    private int readLength;
    private int insertSize;





    private List<easyflow_StringToSampleMap> easyflow_stringtosamplemaps;




    private List<easyflow_StringToReadgroupMap> easyflow_stringtoreadgroupmaps;




    private easyflow_StringToLibraryMap easyflow_stringtolibrarymap;




    private List<easyflow_StringToRecordMap> easyflow_stringtorecordmaps;


    public easyflow_Library(
        String name,        int readLength,        int insertSize    ) {
        super(
        );
        this.name = name;
        this.readLength = readLength;
        this.insertSize = insertSize;
        this.easyflow_stringtosamplemaps = new ArrayList<>();
        this.easyflow_stringtoreadgroupmaps = new ArrayList<>();
        this.easyflow_stringtorecordmaps = new ArrayList<>();
    }

    public easyflow_Library(
        String name,        int readLength,        int insertSize        ArrayList<easyflow_StringToSampleMap> easyflow_stringtosamplemaps,        ArrayList<easyflow_StringToReadgroupMap> easyflow_stringtoreadgroupmaps,        ArrayList<easyflow_StringToRecordMap> easyflow_stringtorecordmaps    ) {
        this.name = name;
        this.readLength = readLength;
        this.insertSize = insertSize;
        this.easyflow_stringtosamplemaps = easyflow_stringtosamplemaps;
        this.easyflow_stringtoreadgroupmaps = easyflow_stringtoreadgroupmaps;
        this.easyflow_stringtorecordmaps = easyflow_stringtorecordmaps;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getReadlength() {
        return readLength;
    }

    public void setReadlength(int readLength) {
        this.readLength = readLength;
    }
    public int getInsertsize() {
        return insertSize;
    }

    public void setInsertsize(int insertSize) {
        this.insertSize = insertSize;
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
    public easyflow_StringToLibraryMap getEasyflow_stringtolibrarymap() {
        return easyflow_stringtolibrarymap;
    }

    public void setEasyflow_stringtolibrarymap(easyflow_StringToLibraryMap easyflow_stringtolibrarymap) {
        this.easyflow_stringtolibrarymap = easyflow_stringtolibrarymap;
    }
    public List<easyflow_StringToRecordMap> getEasyflow_stringtorecordmaps() {
        return easyflow_stringtorecordmaps;
    }

    public void addEasyflow_stringtorecordmap(Easyflow_stringtorecordmap easyflow_stringtorecordmap) {
        this.easyflow_stringtorecordmaps.add(easyflow_stringtorecordmap);
    }

}