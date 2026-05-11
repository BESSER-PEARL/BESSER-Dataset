





import java.util.List;
import java.util.ArrayList;

public class executablemodelingprofile_XClass extends XClassifier {

    private String isExternal;





    private executablemodelingprofile_Class executablemodelingprofile_class;


    public executablemodelingprofile_XClass(
        String isExternal    ) {
        super(
        );
        this.isExternal = isExternal;
    }


    public String getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(String isExternal) {
        this.isExternal = isExternal;
    }

    public executablemodelingprofile_Class getExecutablemodelingprofile_class() {
        return executablemodelingprofile_class;
    }

    public void setExecutablemodelingprofile_class(executablemodelingprofile_Class executablemodelingprofile_class) {
        this.executablemodelingprofile_class = executablemodelingprofile_class;
    }

}