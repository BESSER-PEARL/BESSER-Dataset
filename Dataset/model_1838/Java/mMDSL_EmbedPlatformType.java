





import java.util.List;
import java.util.ArrayList;

public class mMDSL_EmbedPlatformType  {

    private String name;





    private mMDSL_Root mmdsl_root;


    public mMDSL_EmbedPlatformType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mMDSL_Root getMmdsl_root() {
        return mmdsl_root;
    }

    public void setMmdsl_root(mMDSL_Root mmdsl_root) {
        this.mmdsl_root = mmdsl_root;
    }

}