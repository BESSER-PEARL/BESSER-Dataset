





import java.util.List;
import java.util.ArrayList;

public class mtpusecase_Association extends Relation {

    private String targetName;
    private String sourceName;



    public mtpusecase_Association(
        String targetName,        String sourceName    ) {
        super(
        );
        this.targetName = targetName;
        this.sourceName = sourceName;
    }


    public String getTargetname() {
        return targetName;
    }

    public void setTargetname(String targetName) {
        this.targetName = targetName;
    }
    public String getSourcename() {
        return sourceName;
    }

    public void setSourcename(String sourceName) {
        this.sourceName = sourceName;
    }


}