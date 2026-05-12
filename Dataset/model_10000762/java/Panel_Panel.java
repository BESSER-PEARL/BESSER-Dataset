





import java.util.List;
import java.util.ArrayList;

public class Panel_Panel  {

    private None canvas;
    private None button_list;
    private boolean flag_list;



    public Panel_Panel(
        None canvas,        None button_list,        boolean flag_list    ) {
        this.canvas = canvas;
        this.button_list = button_list;
        this.flag_list = flag_list;
    }


    public None getCanvas() {
        return canvas;
    }

    public void setCanvas(None canvas) {
        this.canvas = canvas;
    }
    public None getButton_list() {
        return button_list;
    }

    public void setButton_list(None button_list) {
        this.button_list = button_list;
    }
    public boolean getFlag_list() {
        return flag_list;
    }

    public void setFlag_list(boolean flag_list) {
        this.flag_list = flag_list;
    }


}