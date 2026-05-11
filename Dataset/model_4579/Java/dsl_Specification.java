





import java.util.List;
import java.util.ArrayList;

public class dsl_Specification  {

    private int priority;
    private String specID;





    private dsl_AppMetaData dsl_appmetadata;


    public dsl_Specification(
        int priority,        String specID    ) {
        this.priority = priority;
        this.specID = specID;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public String getSpecid() {
        return specID;
    }

    public void setSpecid(String specID) {
        this.specID = specID;
    }

    public dsl_AppMetaData getDsl_appmetadata() {
        return dsl_appmetadata;
    }

    public void setDsl_appmetadata(dsl_AppMetaData dsl_appmetadata) {
        this.dsl_appmetadata = dsl_appmetadata;
    }

}