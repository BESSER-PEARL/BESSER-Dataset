





import java.util.List;
import java.util.ArrayList;

public class mid_Model extends GenericElement {

    private String fileExtension;
    private String origin;



    public mid_Model(
        String fileExtension,        String origin    ) {
        super(
        );
        this.fileExtension = fileExtension;
        this.origin = origin;
    }


    public String getFileextension() {
        return fileExtension;
    }

    public void setFileextension(String fileExtension) {
        this.fileExtension = fileExtension;
    }
    public String getOrigin() {
        return origin;
    }

    public void setOrigin(String origin) {
        this.origin = origin;
    }


}