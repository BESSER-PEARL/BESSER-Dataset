





import java.util.List;
import java.util.ArrayList;

public class book_Node  {

    private float opacity;
    private boolean enable;
    private String bounds;
    private String background;
    private String foreground;



    public book_Node(
        float opacity,        boolean enable,        String bounds,        String background,        String foreground    ) {
        this.opacity = opacity;
        this.enable = enable;
        this.bounds = bounds;
        this.background = background;
        this.foreground = foreground;
    }


    public float getOpacity() {
        return opacity;
    }

    public void setOpacity(float opacity) {
        this.opacity = opacity;
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


}