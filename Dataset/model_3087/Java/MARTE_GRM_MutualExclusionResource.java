





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_MutualExclusionResource extends Resource {

    private String otherProtectProtocol;
    private String protectKind;



    public MARTE_GRM_MutualExclusionResource(
        String otherProtectProtocol,        String protectKind    ) {
        super(
        );
        this.otherProtectProtocol = otherProtectProtocol;
        this.protectKind = protectKind;
    }


    public String getOtherprotectprotocol() {
        return otherProtectProtocol;
    }

    public void setOtherprotectprotocol(String otherProtectProtocol) {
        this.otherProtectProtocol = otherProtectProtocol;
    }
    public String getProtectkind() {
        return protectKind;
    }

    public void setProtectkind(String protectKind) {
        this.protectKind = protectKind;
    }


}