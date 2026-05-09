





import java.util.List;
import java.util.ArrayList;

public class model_datasources_Query extends Node {

    private String runForCount;
    private String description;



    public model_datasources_Query(
        String runForCount,        String description    ) {
        super(
        );
        this.runForCount = runForCount;
        this.description = description;
    }


    public String getRunforcount() {
        return runForCount;
    }

    public void setRunforcount(String runForCount) {
        this.runForCount = runForCount;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}