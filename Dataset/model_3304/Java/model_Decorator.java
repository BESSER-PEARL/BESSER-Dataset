





import java.util.List;
import java.util.ArrayList;

public class model_Decorator extends Identifiable {

    private float progress;
    private boolean enabled;
    private boolean graphDecorated;



    public model_Decorator(
        float progress,        boolean enabled,        boolean graphDecorated    ) {
        super(
        );
        this.progress = progress;
        this.enabled = enabled;
        this.graphDecorated = graphDecorated;
    }


    public float getProgress() {
        return progress;
    }

    public void setProgress(float progress) {
        this.progress = progress;
    }
    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }
    public boolean getGraphdecorated() {
        return graphDecorated;
    }

    public void setGraphdecorated(boolean graphDecorated) {
        this.graphDecorated = graphDecorated;
    }


}