





import java.util.List;
import java.util.ArrayList;

public class mMDSL_FileWrite  {

    private String append;
    private String filename;
    private String text;





    private mMDSL_FileOperation mmdsl_fileoperation;


    public mMDSL_FileWrite(
        String append,        String filename,        String text    ) {
        this.append = append;
        this.filename = filename;
        this.text = text;
    }


    public String getAppend() {
        return append;
    }

    public void setAppend(String append) {
        this.append = append;
    }
    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public mMDSL_FileOperation getMmdsl_fileoperation() {
        return mmdsl_fileoperation;
    }

    public void setMmdsl_fileoperation(mMDSL_FileOperation mmdsl_fileoperation) {
        this.mmdsl_fileoperation = mmdsl_fileoperation;
    }

}