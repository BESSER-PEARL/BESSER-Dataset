





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwComputing_HwISA extends HwResource {

    private String type;
    private String family;
    private String inst_Width;



    public MARTE_HwComputing_HwISA(
        String type,        String family,        String inst_Width    ) {
        super(
        );
        this.type = type;
        this.family = family;
        this.inst_Width = inst_Width;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getFamily() {
        return family;
    }

    public void setFamily(String family) {
        this.family = family;
    }
    public String getInst_width() {
        return inst_Width;
    }

    public void setInst_width(String inst_Width) {
        this.inst_Width = inst_Width;
    }


}