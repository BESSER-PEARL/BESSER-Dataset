





import java.util.List;
import java.util.ArrayList;

public class spinefm_UserActionModel_UserInit extends UserAction {

    private String confDescription;
    private String pastPath;
    private String filePath;



    public spinefm_UserActionModel_UserInit(
        String confDescription,        String pastPath,        String filePath    ) {
        super(
        );
        this.confDescription = confDescription;
        this.pastPath = pastPath;
        this.filePath = filePath;
    }


    public String getConfdescription() {
        return confDescription;
    }

    public void setConfdescription(String confDescription) {
        this.confDescription = confDescription;
    }
    public String getPastpath() {
        return pastPath;
    }

    public void setPastpath(String pastPath) {
        this.pastPath = pastPath;
    }
    public String getFilepath() {
        return filePath;
    }

    public void setFilepath(String filePath) {
        this.filePath = filePath;
    }


}