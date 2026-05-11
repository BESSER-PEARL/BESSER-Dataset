





import java.util.List;
import java.util.ArrayList;

public class softwaretraces_Model extends MyNode {

    private String resourceFileName;



    public softwaretraces_Model(
        String resourceFileName    ) {
        super(
        );
        this.resourceFileName = resourceFileName;
    }


    public String getResourcefilename() {
        return resourceFileName;
    }

    public void setResourcefilename(String resourceFileName) {
        this.resourceFileName = resourceFileName;
    }


}