





import java.util.List;
import java.util.ArrayList;

public class draw2d_Figure  {

    private String minimumSize;
    private boolean focusTraversable;
    private boolean visible;
    private String preferredSize;
    private boolean opaque;
    private boolean enabled;
    private String bounds;
    private String maximumSize;





    private draw2d_Color draw2d_color;




    private draw2d_Color draw2d_color;




    private List<draw2d_Figure> draw2d_figures;




    private draw2d_Figure draw2d_figure;




    private draw2d_Figure draw2d_figure;




    private draw2d_Draw2DCanvas draw2d_draw2dcanvas;




    private draw2d_Font draw2d_font;




    private draw2d_Border draw2d_border;


    public draw2d_Figure(
        String minimumSize,        boolean focusTraversable,        boolean visible,        String preferredSize,        boolean opaque,        boolean enabled,        String bounds,        String maximumSize    ) {
        this.minimumSize = minimumSize;
        this.focusTraversable = focusTraversable;
        this.visible = visible;
        this.preferredSize = preferredSize;
        this.opaque = opaque;
        this.enabled = enabled;
        this.bounds = bounds;
        this.maximumSize = maximumSize;
        this.draw2d_figures = new ArrayList<>();
    }

    public draw2d_Figure(
        String minimumSize,        boolean focusTraversable,        boolean visible,        String preferredSize,        boolean opaque,        boolean enabled,        String bounds,        String maximumSize        ArrayList<draw2d_Figure> draw2d_figures    ) {
        this.minimumSize = minimumSize;
        this.focusTraversable = focusTraversable;
        this.visible = visible;
        this.preferredSize = preferredSize;
        this.opaque = opaque;
        this.enabled = enabled;
        this.bounds = bounds;
        this.maximumSize = maximumSize;
        this.draw2d_figures = draw2d_figures;
    }

    public String getMinimumsize() {
        return minimumSize;
    }

    public void setMinimumsize(String minimumSize) {
        this.minimumSize = minimumSize;
    }
    public boolean getFocustraversable() {
        return focusTraversable;
    }

    public void setFocustraversable(boolean focusTraversable) {
        this.focusTraversable = focusTraversable;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public String getPreferredsize() {
        return preferredSize;
    }

    public void setPreferredsize(String preferredSize) {
        this.preferredSize = preferredSize;
    }
    public boolean getOpaque() {
        return opaque;
    }

    public void setOpaque(boolean opaque) {
        this.opaque = opaque;
    }
    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }
    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }
    public String getMaximumsize() {
        return maximumSize;
    }

    public void setMaximumsize(String maximumSize) {
        this.maximumSize = maximumSize;
    }

    public draw2d_Color getDraw2d_color() {
        return draw2d_color;
    }

    public void setDraw2d_color(draw2d_Color draw2d_color) {
        this.draw2d_color = draw2d_color;
    }
    public draw2d_Color getDraw2d_color() {
        return draw2d_color;
    }

    public void setDraw2d_color(draw2d_Color draw2d_color) {
        this.draw2d_color = draw2d_color;
    }
    public List<draw2d_Figure> getDraw2d_figures() {
        return draw2d_figures;
    }

    public void addDraw2d_figure(Draw2d_figure draw2d_figure) {
        this.draw2d_figures.add(draw2d_figure);
    }
    public draw2d_Figure getDraw2d_figure() {
        return draw2d_figure;
    }

    public void setDraw2d_figure(draw2d_Figure draw2d_figure) {
        this.draw2d_figure = draw2d_figure;
    }
    public draw2d_Figure getDraw2d_figure() {
        return draw2d_figure;
    }

    public void setDraw2d_figure(draw2d_Figure draw2d_figure) {
        this.draw2d_figure = draw2d_figure;
    }
    public draw2d_Draw2DCanvas getDraw2d_draw2dcanvas() {
        return draw2d_draw2dcanvas;
    }

    public void setDraw2d_draw2dcanvas(draw2d_Draw2DCanvas draw2d_draw2dcanvas) {
        this.draw2d_draw2dcanvas = draw2d_draw2dcanvas;
    }
    public draw2d_Font getDraw2d_font() {
        return draw2d_font;
    }

    public void setDraw2d_font(draw2d_Font draw2d_font) {
        this.draw2d_font = draw2d_font;
    }
    public draw2d_Border getDraw2d_border() {
        return draw2d_border;
    }

    public void setDraw2d_border(draw2d_Border draw2d_border) {
        this.draw2d_border = draw2d_border;
    }

}