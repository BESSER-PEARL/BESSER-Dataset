





import java.util.List;
import java.util.ArrayList;

public class mid_Model extends GenericElement {

    private String fileExtension;
    private String origin;





    private mid_MID mid_mid;


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

    public mid_MID getMid_mid() {
        return mid_mid;
    }

    public void setMid_mid(mid_MID mid_mid) {
        this.mid_mid = mid_mid;
    }

}