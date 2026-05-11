





import java.util.List;
import java.util.ArrayList;

public class pimm_Refinement extends PiMMVisitable {

    private String filePath;
    private String fileName;



    public pimm_Refinement(
        String filePath,        String fileName    ) {
        super(
        );
        this.filePath = filePath;
        this.fileName = fileName;
    }


    public String getFilepath() {
        return filePath;
    }

    public void setFilepath(String filePath) {
        this.filePath = filePath;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }


}