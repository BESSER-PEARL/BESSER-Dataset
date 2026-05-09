





import java.util.List;
import java.util.ArrayList;

public class book_Node  {

    private String background;
    private String foreground;
    private boolean enable;
    private String bounds;
    private float opacity;



    public book_Node(
        String background,        String foreground,        boolean enable,        String bounds,        float opacity    ) {
        this.background = background;
        this.foreground = foreground;
        this.enable = enable;
        this.bounds = bounds;
        this.opacity = opacity;
    }


    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getForeground() {
        return foreground;
    }

    public void setForeground(String foreground) {
        this.foreground = foreground;
    }
    public boolean getEnable() {
        return enable;
    }

    public void setEnable(boolean enable) {
        this.enable = enable;
    }
    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }
    public float getOpacity() {
        return opacity;
    }

    public void setOpacity(float opacity) {
        this.opacity = opacity;
    }


}