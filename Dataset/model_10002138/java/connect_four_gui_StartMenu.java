





import java.util.List;
import java.util.ArrayList;

public class connect_four_gui_StartMenu  {

    private None bp;
    private None startLabel;
    private None label;
    private String window;
    private None bStart;
    private None bPlay;



    public connect_four_gui_StartMenu(
        None bp,        None startLabel,        None label,        String window,        None bStart,        None bPlay    ) {
        this.bp = bp;
        this.startLabel = startLabel;
        this.label = label;
        this.window = window;
        this.bStart = bStart;
        this.bPlay = bPlay;
    }


    public None getBp() {
        return bp;
    }

    public void setBp(None bp) {
        this.bp = bp;
    }
    public None getStartlabel() {
        return startLabel;
    }

    public void setStartlabel(None startLabel) {
        this.startLabel = startLabel;
    }
    public None getLabel() {
        return label;
    }

    public void setLabel(None label) {
        this.label = label;
    }
    public String getWindow() {
        return window;
    }

    public void setWindow(String window) {
        this.window = window;
    }
    public None getBstart() {
        return bStart;
    }

    public void setBstart(None bStart) {
        this.bStart = bStart;
    }
    public None getBplay() {
        return bPlay;
    }

    public void setBplay(None bPlay) {
        this.bPlay = bPlay;
    }


}