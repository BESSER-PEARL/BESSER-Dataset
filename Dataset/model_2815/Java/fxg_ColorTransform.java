





import java.util.List;
import java.util.ArrayList;

public class fxg_ColorTransform extends FXGElement {

    private String alphaMultiplier;
    private String greenOffset;
    private String redMultiplier;
    private String blueOffset;
    private String greenMultiplier;
    private String blueMultiplier;
    private String redOffset;
    private String alphaOffset;



    public fxg_ColorTransform(
        String alphaMultiplier,        String greenOffset,        String redMultiplier,        String blueOffset,        String greenMultiplier,        String blueMultiplier,        String redOffset,        String alphaOffset    ) {
        super(
        );
        this.alphaMultiplier = alphaMultiplier;
        this.greenOffset = greenOffset;
        this.redMultiplier = redMultiplier;
        this.blueOffset = blueOffset;
        this.greenMultiplier = greenMultiplier;
        this.blueMultiplier = blueMultiplier;
        this.redOffset = redOffset;
        this.alphaOffset = alphaOffset;
    }


    public String getAlphamultiplier() {
        return alphaMultiplier;
    }

    public void setAlphamultiplier(String alphaMultiplier) {
        this.alphaMultiplier = alphaMultiplier;
    }
    public String getGreenoffset() {
        return greenOffset;
    }

    public void setGreenoffset(String greenOffset) {
        this.greenOffset = greenOffset;
    }
    public String getRedmultiplier() {
        return redMultiplier;
    }

    public void setRedmultiplier(String redMultiplier) {
        this.redMultiplier = redMultiplier;
    }
    public String getBlueoffset() {
        return blueOffset;
    }

    public void setBlueoffset(String blueOffset) {
        this.blueOffset = blueOffset;
    }
    public String getGreenmultiplier() {
        return greenMultiplier;
    }

    public void setGreenmultiplier(String greenMultiplier) {
        this.greenMultiplier = greenMultiplier;
    }
    public String getBluemultiplier() {
        return blueMultiplier;
    }

    public void setBluemultiplier(String blueMultiplier) {
        this.blueMultiplier = blueMultiplier;
    }
    public String getRedoffset() {
        return redOffset;
    }

    public void setRedoffset(String redOffset) {
        this.redOffset = redOffset;
    }
    public String getAlphaoffset() {
        return alphaOffset;
    }

    public void setAlphaoffset(String alphaOffset) {
        this.alphaOffset = alphaOffset;
    }


}