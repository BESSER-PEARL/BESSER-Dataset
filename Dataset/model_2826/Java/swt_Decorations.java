





import java.util.List;
import java.util.ArrayList;

public class swt_Decorations extends Canvas {

    private boolean maximized;
    private boolean minimized;



    public swt_Decorations(
        boolean maximized,        boolean minimized    ) {
        super(
        );
        this.maximized = maximized;
        this.minimized = minimized;
    }


    public boolean getMaximized() {
        return maximized;
    }

    public void setMaximized(boolean maximized) {
        this.maximized = maximized;
    }
    public boolean getMinimized() {
        return minimized;
    }

    public void setMinimized(boolean minimized) {
        this.minimized = minimized;
    }


}