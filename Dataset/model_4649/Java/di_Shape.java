





import java.util.List;
import java.util.ArrayList;

public class di_Shape extends Container, Node {

    private int background;
    private int foreground;
    private String bounds;





    private di_Container di_container;


    public di_Shape(
        int background,        int foreground,        String bounds    ) {
        super(
        );
        this.background = background;
        this.foreground = foreground;
        this.bounds = bounds;
    }


    public int getBackground() {
        return background;
    }

    public void setBackground(int background) {
        this.background = background;
    }
    public int getForeground() {
        return foreground;
    }

    public void setForeground(int foreground) {
        this.foreground = foreground;
    }
    public String getBounds() {
        return bounds;
    }

    public void setBounds(String bounds) {
        this.bounds = bounds;
    }

    public di_Container getDi_container() {
        return di_container;
    }

    public void setDi_container(di_Container di_container) {
        this.di_container = di_container;
    }

}