





import java.util.List;
import java.util.ArrayList;

public class fxg_BlurFilter extends Filter {

    private String blurX;
    private String blurY;
    private String quality;



    public fxg_BlurFilter(
        String blurX,        String blurY,        String quality    ) {
        super(
        );
        this.blurX = blurX;
        this.blurY = blurY;
        this.quality = quality;
    }


    public String getBlurx() {
        return blurX;
    }

    public void setBlurx(String blurX) {
        this.blurX = blurX;
    }
    public String getBlury() {
        return blurY;
    }

    public void setBlury(String blurY) {
        this.blurY = blurY;
    }
    public String getQuality() {
        return quality;
    }

    public void setQuality(String quality) {
        this.quality = quality;
    }


}