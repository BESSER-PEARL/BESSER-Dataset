





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_ColorPin extends Pin {

    private boolean backgroundNotForeground;



    public gmfgraph_ColorPin(
        boolean backgroundNotForeground    ) {
        super(
        );
        this.backgroundNotForeground = backgroundNotForeground;
    }


    public boolean getBackgroundnotforeground() {
        return backgroundNotForeground;
    }

    public void setBackgroundnotforeground(boolean backgroundNotForeground) {
        this.backgroundNotForeground = backgroundNotForeground;
    }


}