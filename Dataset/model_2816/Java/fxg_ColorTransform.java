





import java.util.List;
import java.util.ArrayList;

public class fxg_ColorTransform extends FXGElement {

    private String redMultiplier;
    private String redOffset;
    private String blueOffset;
    private String greenOffset;
    private String greenMultiplier;
    private String alphaOffset;
    private String alphaMultiplier;
    private String blueMultiplier;



    public fxg_ColorTransform(
        String redMultiplier,        String redOffset,        String blueOffset,        String greenOffset,        String greenMultiplier,        String alphaOffset,        String alphaMultiplier,        String blueMultiplier    ) {
        super(
        );
        this.redMultiplier = redMultiplier;
        this.redOffset = redOffset;
        this.blueOffset = blueOffset;
        this.greenOffset = greenOffset;
        this.greenMultiplier = greenMultiplier;
        this.alphaOffset = alphaOffset;
        this.alphaMultiplier = alphaMultiplier;
        this.blueMultiplier = blueMultiplier;
    }


    public String getRedmultiplier() {
        return redMultiplier;
    }

    public void setRedmultiplier(String redMultiplier) {
        this.redMultiplier = redMultiplier;
    }
    public String getRedoffset() {
        return redOffset;
    }

    public void setRedoffset(String redOffset) {
        this.redOffset = redOffset;
    }
    public String getBlueoffset() {
        return blueOffset;
    }

    public void setBlueoffset(String blueOffset) {
        this.blueOffset = blueOffset;
    }
    public String getGreenoffset() {
        return greenOffset;
    }

    public void setGreenoffset(String greenOffset) {
        this.greenOffset = greenOffset;
    }
    public String getGreenmultiplier() {
        return greenMultiplier;
    }

    public void setGreenmultiplier(String greenMultiplier) {
        this.greenMultiplier = greenMultiplier;
    }
    public String getAlphaoffset() {
        return alphaOffset;
    }

    public void setAlphaoffset(String alphaOffset) {
        this.alphaOffset = alphaOffset;
    }
    public String getAlphamultiplier() {
        return alphaMultiplier;
    }

    public void setAlphamultiplier(String alphaMultiplier) {
        this.alphaMultiplier = alphaMultiplier;
    }
    public String getBluemultiplier() {
        return blueMultiplier;
    }

    public void setBluemultiplier(String blueMultiplier) {
        this.blueMultiplier = blueMultiplier;
    }


}