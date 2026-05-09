





import java.util.List;
import java.util.ArrayList;

public class UMLModel_LinkEndCreationData extends LinkEndData {

    private String insertAt;
    private String isReplaceAll;



    public UMLModel_LinkEndCreationData(
        String insertAt,        String isReplaceAll    ) {
        super(
        );
        this.insertAt = insertAt;
        this.isReplaceAll = isReplaceAll;
    }


    public String getInsertat() {
        return insertAt;
    }

    public void setInsertat(String insertAt) {
        this.insertAt = insertAt;
    }
    public String getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(String isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }


}