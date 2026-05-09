





import java.util.List;
import java.util.ArrayList;

public class easyflow_StringToLibraryMap  {

    private String key;





    private easyflow_Library easyflow_library;




    private easyflow_Readgroup easyflow_readgroup;




    private easyflow_Group easyflow_group;




    private easyflow_Sample easyflow_sample;


    public easyflow_StringToLibraryMap(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public easyflow_Library getEasyflow_library() {
        return easyflow_library;
    }

    public void setEasyflow_library(easyflow_Library easyflow_library) {
        this.easyflow_library = easyflow_library;
    }
    public easyflow_Readgroup getEasyflow_readgroup() {
        return easyflow_readgroup;
    }

    public void setEasyflow_readgroup(easyflow_Readgroup easyflow_readgroup) {
        this.easyflow_readgroup = easyflow_readgroup;
    }
    public easyflow_Group getEasyflow_group() {
        return easyflow_group;
    }

    public void setEasyflow_group(easyflow_Group easyflow_group) {
        this.easyflow_group = easyflow_group;
    }
    public easyflow_Sample getEasyflow_sample() {
        return easyflow_sample;
    }

    public void setEasyflow_sample(easyflow_Sample easyflow_sample) {
        this.easyflow_sample = easyflow_sample;
    }

}