





import java.util.List;
import java.util.ArrayList;

public class model_Image extends Widget, BorderSupport, FlipSupport, RotationSupport, LinkSupport {

    private String src;
    private boolean grayscale;



    public model_Image(
        String src,        boolean grayscale    ) {
        super(
        );
        this.src = src;
        this.grayscale = grayscale;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public boolean getGrayscale() {
        return grayscale;
    }

    public void setGrayscale(boolean grayscale) {
        this.grayscale = grayscale;
    }


}