





import java.util.List;
import java.util.ArrayList;

public class model_datasources_Query extends Node {

    private String description;
    private String runForCount;



    public model_datasources_Query(
        String description,        String runForCount    ) {
        super(
        );
        this.description = description;
        this.runForCount = runForCount;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getRunforcount() {
        return runForCount;
    }

    public void setRunforcount(String runForCount) {
        this.runForCount = runForCount;
    }


}