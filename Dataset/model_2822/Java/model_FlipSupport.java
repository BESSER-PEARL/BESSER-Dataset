





import java.util.List;
import java.util.ArrayList;

public class model_FlipSupport  {

    private boolean vFlip;
    private boolean hFlip;



    public model_FlipSupport(
        boolean vFlip,        boolean hFlip    ) {
        this.vFlip = vFlip;
        this.hFlip = hFlip;
    }


    public boolean getVflip() {
        return vFlip;
    }

    public void setVflip(boolean vFlip) {
        this.vFlip = vFlip;
    }
    public boolean getHflip() {
        return hFlip;
    }

    public void setHflip(boolean hFlip) {
        this.hFlip = hFlip;
    }


}