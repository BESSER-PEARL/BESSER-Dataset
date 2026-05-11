





import java.util.List;
import java.util.ArrayList;

public class krendering_KXPosition  {

    private float relative;
    private float absolute;



    public krendering_KXPosition(
        float relative,        float absolute    ) {
        this.relative = relative;
        this.absolute = absolute;
    }


    public float getRelative() {
        return relative;
    }

    public void setRelative(float relative) {
        this.relative = relative;
    }
    public float getAbsolute() {
        return absolute;
    }

    public void setAbsolute(float absolute) {
        this.absolute = absolute;
    }


}