





import java.util.List;
import java.util.ArrayList;

public class mMDSL_IncludeLibrary  {

    private String name;





    private mMDSL_Root mmdsl_root;




    private mMDSL_IncludeLibraryType mmdsl_includelibrarytype;


    public mMDSL_IncludeLibrary(
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
    public mMDSL_IncludeLibraryType getMmdsl_includelibrarytype() {
        return mmdsl_includelibrarytype;
    }

    public void setMmdsl_includelibrarytype(mMDSL_IncludeLibraryType mmdsl_includelibrarytype) {
        this.mmdsl_includelibrarytype = mmdsl_includelibrarytype;
    }

}