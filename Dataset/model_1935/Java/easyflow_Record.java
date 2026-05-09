





import java.util.List;
import java.util.ArrayList;

public class easyflow_Record extends GroupingCriterion {

    private String fileNames;
    private String refData;





    private easyflow_Library easyflow_library;


    public easyflow_Record(
        String fileNames,        String refData    ) {
        super(
        );
        this.fileNames = fileNames;
        this.refData = refData;
    }


    public String getFilenames() {
        return fileNames;
    }

    public void setFilenames(String fileNames) {
        this.fileNames = fileNames;
    }
    public String getRefdata() {
        return refData;
    }

    public void setRefdata(String refData) {
        this.refData = refData;
    }

    public easyflow_Library getEasyflow_library() {
        return easyflow_library;
    }

    public void setEasyflow_library(easyflow_Library easyflow_library) {
        this.easyflow_library = easyflow_library;
    }

}