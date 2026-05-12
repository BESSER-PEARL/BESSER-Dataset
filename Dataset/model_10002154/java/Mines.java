





import java.util.List;
import java.util.ArrayList;

public class Mines  {

    private None hexCell;
    private int FRAME_WIDTH;
    private None timeBar;
    private None statusbar;
    private int FRAME_HEIGHT;



    public Mines(
        None hexCell,        int FRAME_WIDTH,        None timeBar,        None statusbar,        int FRAME_HEIGHT    ) {
        this.hexCell = hexCell;
        this.FRAME_WIDTH = FRAME_WIDTH;
        this.timeBar = timeBar;
        this.statusbar = statusbar;
        this.FRAME_HEIGHT = FRAME_HEIGHT;
    }


    public None getHexcell() {
        return hexCell;
    }

    public void setHexcell(None hexCell) {
        this.hexCell = hexCell;
    }
    public int getFrame_width() {
        return FRAME_WIDTH;
    }

    public void setFrame_width(int FRAME_WIDTH) {
        this.FRAME_WIDTH = FRAME_WIDTH;
    }
    public None getTimebar() {
        return timeBar;
    }

    public void setTimebar(None timeBar) {
        this.timeBar = timeBar;
    }
    public None getStatusbar() {
        return statusbar;
    }

    public void setStatusbar(None statusbar) {
        this.statusbar = statusbar;
    }
    public int getFrame_height() {
        return FRAME_HEIGHT;
    }

    public void setFrame_height(int FRAME_HEIGHT) {
        this.FRAME_HEIGHT = FRAME_HEIGHT;
    }


}