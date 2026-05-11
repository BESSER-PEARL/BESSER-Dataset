





import java.util.List;
import java.util.ArrayList;

public class form_SuggestBox extends MultipleValuatedFormField {

    private boolean useMaxItems;
    private boolean asynchronous;
    private int maxItems;
    private int delay;



    public form_SuggestBox(
        boolean useMaxItems,        boolean asynchronous,        int maxItems,        int delay    ) {
        super(
        );
        this.useMaxItems = useMaxItems;
        this.asynchronous = asynchronous;
        this.maxItems = maxItems;
        this.delay = delay;
    }


    public boolean getUsemaxitems() {
        return useMaxItems;
    }

    public void setUsemaxitems(boolean useMaxItems) {
        this.useMaxItems = useMaxItems;
    }
    public boolean getAsynchronous() {
        return asynchronous;
    }

    public void setAsynchronous(boolean asynchronous) {
        this.asynchronous = asynchronous;
    }
    public int getMaxitems() {
        return maxItems;
    }

    public void setMaxitems(int maxItems) {
        this.maxItems = maxItems;
    }
    public int getDelay() {
        return delay;
    }

    public void setDelay(int delay) {
        this.delay = delay;
    }


}