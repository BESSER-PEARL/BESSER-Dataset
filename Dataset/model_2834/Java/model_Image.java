





import java.util.List;
import java.util.ArrayList;

public class model_Image extends RotationSupport, LinkSupport, BorderSupport, Widget, FlipSupport {

    private boolean grayscale;
    private String src;



    public model_Image(
        boolean grayscale,        String src    ) {
        super(
        );
        this.grayscale = grayscale;
        this.src = src;
    }


    public boolean getGrayscale() {
        return grayscale;
    }

    public void setGrayscale(boolean grayscale) {
        this.grayscale = grayscale;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}