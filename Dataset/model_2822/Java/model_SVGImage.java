





import java.util.List;
import java.util.ArrayList;

public class model_SVGImage extends Widget, RotationSupport, FlipSupport, LinkSupport, ColorBackgroundSupport, ColorAlphaSupport, ColorForegroundSupport {

    private String src;



    public model_SVGImage(
        String src    ) {
        super(
        );
        this.src = src;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}