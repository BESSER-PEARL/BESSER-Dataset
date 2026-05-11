





import java.util.List;
import java.util.ArrayList;

public class thingml_Region extends AnnotatedElement {

    private boolean history;



    public thingml_Region(
        boolean history    ) {
        super(
        );
        this.history = history;
    }


    public boolean getHistory() {
        return history;
    }

    public void setHistory(boolean history) {
        this.history = history;
    }


}