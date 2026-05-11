





import java.util.List;
import java.util.ArrayList;

public class krendering_KXPosition  {

    private float absolute;
    private float relative;



    public krendering_KXPosition(
        float absolute,        float relative    ) {
        this.absolute = absolute;
        this.relative = relative;
    }


    public float getAbsolute() {
        return absolute;
    }

    public void setAbsolute(float absolute) {
        this.absolute = absolute;
    }
    public float getRelative() {
        return relative;
    }

    public void setRelative(float relative) {
        this.relative = relative;
    }


}