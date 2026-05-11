





import java.util.List;
import java.util.ArrayList;

public class afpText_ColorManagementResourceDescriptor extends triplet {

    private String CMRScpe;
    private String ProcMode;



    public afpText_ColorManagementResourceDescriptor(
        String CMRScpe,        String ProcMode    ) {
        super(
        );
        this.CMRScpe = CMRScpe;
        this.ProcMode = ProcMode;
    }


    public String getCmrscpe() {
        return CMRScpe;
    }

    public void setCmrscpe(String CMRScpe) {
        this.CMRScpe = CMRScpe;
    }
    public String getProcmode() {
        return ProcMode;
    }

    public void setProcmode(String ProcMode) {
        this.ProcMode = ProcMode;
    }


}