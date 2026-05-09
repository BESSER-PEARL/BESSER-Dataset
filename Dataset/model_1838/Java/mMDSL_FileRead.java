





import java.util.List;
import java.util.ArrayList;

public class mMDSL_FileRead  {

    private String filename;





    private mMDSL_FileOperation mmdsl_fileoperation;


    public mMDSL_FileRead(
        String filename    ) {
        this.filename = filename;
    }


    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }

    public mMDSL_FileOperation getMmdsl_fileoperation() {
        return mmdsl_fileoperation;
    }

    public void setMmdsl_fileoperation(mMDSL_FileOperation mmdsl_fileoperation) {
        this.mmdsl_fileoperation = mmdsl_fileoperation;
    }

}