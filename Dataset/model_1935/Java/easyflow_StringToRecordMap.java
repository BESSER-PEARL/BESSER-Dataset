





import java.util.List;
import java.util.ArrayList;

public class easyflow_StringToRecordMap  {

    private String key;





    private easyflow_Group easyflow_group;




    private easyflow_Record easyflow_record;




    private easyflow_Sample easyflow_sample;




    private easyflow_Library easyflow_library;


    public easyflow_StringToRecordMap(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public easyflow_Group getEasyflow_group() {
        return easyflow_group;
    }

    public void setEasyflow_group(easyflow_Group easyflow_group) {
        this.easyflow_group = easyflow_group;
    }
    public easyflow_Record getEasyflow_record() {
        return easyflow_record;
    }

    public void setEasyflow_record(easyflow_Record easyflow_record) {
        this.easyflow_record = easyflow_record;
    }
    public easyflow_Sample getEasyflow_sample() {
        return easyflow_sample;
    }

    public void setEasyflow_sample(easyflow_Sample easyflow_sample) {
        this.easyflow_sample = easyflow_sample;
    }
    public easyflow_Library getEasyflow_library() {
        return easyflow_library;
    }

    public void setEasyflow_library(easyflow_Library easyflow_library) {
        this.easyflow_library = easyflow_library;
    }

}