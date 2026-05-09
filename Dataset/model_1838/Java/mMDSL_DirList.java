





import java.util.List;
import java.util.ArrayList;

public class mMDSL_DirList  {

    private String dirname;





    private mMDSL_DirOperation mmdsl_diroperation;


    public mMDSL_DirList(
        String dirname    ) {
        this.dirname = dirname;
    }


    public String getDirname() {
        return dirname;
    }

    public void setDirname(String dirname) {
        this.dirname = dirname;
    }

    public mMDSL_DirOperation getMmdsl_diroperation() {
        return mmdsl_diroperation;
    }

    public void setMmdsl_diroperation(mMDSL_DirOperation mmdsl_diroperation) {
        this.mmdsl_diroperation = mmdsl_diroperation;
    }

}