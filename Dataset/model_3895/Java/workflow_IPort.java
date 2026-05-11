





import java.util.List;
import java.util.ArrayList;

public class workflow_IPort extends IWorkflowElement {

    private String fileName;



    public workflow_IPort(
        String fileName    ) {
        super(
        );
        this.fileName = fileName;
    }


    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }


}