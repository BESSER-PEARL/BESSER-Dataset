





import java.util.List;
import java.util.ArrayList;

public class mMDSL_FileCopy  {

    private String dest;
    private String src;





    private mMDSL_FileOperation mmdsl_fileoperation;


    public mMDSL_FileCopy(
        String dest,        String src    ) {
        this.dest = dest;
        this.src = src;
    }


    public String getDest() {
        return dest;
    }

    public void setDest(String dest) {
        this.dest = dest;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }

    public mMDSL_FileOperation getMmdsl_fileoperation() {
        return mmdsl_fileoperation;
    }

    public void setMmdsl_fileoperation(mMDSL_FileOperation mmdsl_fileoperation) {
        this.mmdsl_fileoperation = mmdsl_fileoperation;
    }

}