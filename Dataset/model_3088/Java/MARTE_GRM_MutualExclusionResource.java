





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_MutualExclusionResource extends Resource {

    private String ceiling;
    private String protectKind;
    private String otherProtectProtocol;



    public MARTE_GRM_MutualExclusionResource(
        String ceiling,        String protectKind,        String otherProtectProtocol    ) {
        super(
        );
        this.ceiling = ceiling;
        this.protectKind = protectKind;
        this.otherProtectProtocol = otherProtectProtocol;
    }


    public String getCeiling() {
        return ceiling;
    }

    public void setCeiling(String ceiling) {
        this.ceiling = ceiling;
    }
    public String getProtectkind() {
        return protectKind;
    }

    public void setProtectkind(String protectKind) {
        this.protectKind = protectKind;
    }
    public String getOtherprotectprotocol() {
        return otherProtectProtocol;
    }

    public void setOtherprotectprotocol(String otherProtectProtocol) {
        this.otherProtectProtocol = otherProtectProtocol;
    }


}