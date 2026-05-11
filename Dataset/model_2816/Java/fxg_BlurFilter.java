





import java.util.List;
import java.util.ArrayList;

public class fxg_BlurFilter extends Filter {

    private String quality;
    private String blurY;
    private String blurX;



    public fxg_BlurFilter(
        String quality,        String blurY,        String blurX    ) {
        super(
        );
        this.quality = quality;
        this.blurY = blurY;
        this.blurX = blurX;
    }


    public String getQuality() {
        return quality;
    }

    public void setQuality(String quality) {
        this.quality = quality;
    }
    public String getBlury() {
        return blurY;
    }

    public void setBlury(String blurY) {
        this.blurY = blurY;
    }
    public String getBlurx() {
        return blurX;
    }

    public void setBlurx(String blurX) {
        this.blurX = blurX;
    }


}