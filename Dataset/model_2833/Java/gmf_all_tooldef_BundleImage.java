





import java.util.List;
import java.util.ArrayList;

public class gmf_all_tooldef_BundleImage extends Image {

    private String bundle;
    private String path;



    public gmf_all_tooldef_BundleImage(
        String bundle,        String path    ) {
        super(
        );
        this.bundle = bundle;
        this.path = path;
    }


    public String getBundle() {
        return bundle;
    }

    public void setBundle(String bundle) {
        this.bundle = bundle;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}