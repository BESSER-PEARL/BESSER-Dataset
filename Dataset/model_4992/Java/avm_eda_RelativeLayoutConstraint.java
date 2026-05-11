





import java.util.List;
import java.util.ArrayList;

public class avm_eda_RelativeLayoutConstraint extends PcbLayoutConstraint {

    private String RelativeLayer;
    private String YOffset;
    private String XOffset;
    private String RelativeRotation;



    public avm_eda_RelativeLayoutConstraint(
        String RelativeLayer,        String YOffset,        String XOffset,        String RelativeRotation    ) {
        super(
        );
        this.RelativeLayer = RelativeLayer;
        this.YOffset = YOffset;
        this.XOffset = XOffset;
        this.RelativeRotation = RelativeRotation;
    }


    public String getRelativelayer() {
        return RelativeLayer;
    }

    public void setRelativelayer(String RelativeLayer) {
        this.RelativeLayer = RelativeLayer;
    }
    public String getYoffset() {
        return YOffset;
    }

    public void setYoffset(String YOffset) {
        this.YOffset = YOffset;
    }
    public String getXoffset() {
        return XOffset;
    }

    public void setXoffset(String XOffset) {
        this.XOffset = XOffset;
    }
    public String getRelativerotation() {
        return RelativeRotation;
    }

    public void setRelativerotation(String RelativeRotation) {
        this.RelativeRotation = RelativeRotation;
    }


}