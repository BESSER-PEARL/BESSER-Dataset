





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_CoatOfArmsType  {

    private String name;
    private String mask;
    private String effect;
    private String sealOverlay;
    private String frame;



    public ck2gfx_CoatOfArmsType(
        String name,        String mask,        String effect,        String sealOverlay,        String frame    ) {
        this.name = name;
        this.mask = mask;
        this.effect = effect;
        this.sealOverlay = sealOverlay;
        this.frame = frame;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMask() {
        return mask;
    }

    public void setMask(String mask) {
        this.mask = mask;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }
    public String getSealoverlay() {
        return sealOverlay;
    }

    public void setSealoverlay(String sealOverlay) {
        this.sealOverlay = sealOverlay;
    }
    public String getFrame() {
        return frame;
    }

    public void setFrame(String frame) {
        this.frame = frame;
    }


}