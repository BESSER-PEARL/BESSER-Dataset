





import java.util.List;
import java.util.ArrayList;

public class easyflow_Record extends GroupingCriterion {

    private String refData;
    private String fileNames;





    private easyflow_StringToRecordMap easyflow_stringtorecordmap;




    private easyflow_Readgroup easyflow_readgroup;




    private easyflow_Library easyflow_library;




    private easyflow_Sample easyflow_sample;


    public easyflow_Record(
        String refData,        String fileNames    ) {
        super(
        );
        this.refData = refData;
        this.fileNames = fileNames;
    }


    public String getRefdata() {
        return refData;
    }

    public void setRefdata(String refData) {
        this.refData = refData;
    }
    public String getFilenames() {
        return fileNames;
    }

    public void setFilenames(String fileNames) {
        this.fileNames = fileNames;
    }

    public easyflow_StringToRecordMap getEasyflow_stringtorecordmap() {
        return easyflow_stringtorecordmap;
    }

    public void setEasyflow_stringtorecordmap(easyflow_StringToRecordMap easyflow_stringtorecordmap) {
        this.easyflow_stringtorecordmap = easyflow_stringtorecordmap;
    }
    public easyflow_Readgroup getEasyflow_readgroup() {
        return easyflow_readgroup;
    }

    public void setEasyflow_readgroup(easyflow_Readgroup easyflow_readgroup) {
        this.easyflow_readgroup = easyflow_readgroup;
    }
    public easyflow_Library getEasyflow_library() {
        return easyflow_library;
    }

    public void setEasyflow_library(easyflow_Library easyflow_library) {
        this.easyflow_library = easyflow_library;
    }
    public easyflow_Sample getEasyflow_sample() {
        return easyflow_sample;
    }

    public void setEasyflow_sample(easyflow_Sample easyflow_sample) {
        this.easyflow_sample = easyflow_sample;
    }

}