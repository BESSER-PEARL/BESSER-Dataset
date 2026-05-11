





import java.util.List;
import java.util.ArrayList;

public class avm_eda_RelativeLayoutConstraint extends PcbLayoutConstraint {

    private String XOffset;
    private String YOffset;
    private String RelativeRotation;
    private String RelativeLayer;



    public avm_eda_RelativeLayoutConstraint(
        String XOffset,        String YOffset,        String RelativeRotation,        String RelativeLayer    ) {
        super(
        );
        this.XOffset = XOffset;
        this.YOffset = YOffset;
        this.RelativeRotation = RelativeRotation;
        this.RelativeLayer = RelativeLayer;
    }


    public String getXoffset() {
        return XOffset;
    }

    public void setXoffset(String XOffset) {
        this.XOffset = XOffset;
    }
    public String getYoffset() {
        return YOffset;
    }

    public void setYoffset(String YOffset) {
        this.YOffset = YOffset;
    }
    public String getRelativerotation() {
        return RelativeRotation;
    }

    public void setRelativerotation(String RelativeRotation) {
        this.RelativeRotation = RelativeRotation;
    }
    public String getRelativelayer() {
        return RelativeLayer;
    }

    public void setRelativelayer(String RelativeLayer) {
        this.RelativeLayer = RelativeLayer;
    }


}