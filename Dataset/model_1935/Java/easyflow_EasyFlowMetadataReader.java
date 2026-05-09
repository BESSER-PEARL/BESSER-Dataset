





import java.util.List;
import java.util.ArrayList;

public class easyflow_EasyFlowMetadataReader extends EasyFlowMetadata {

    private String fileName;



    public easyflow_EasyFlowMetadataReader(
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