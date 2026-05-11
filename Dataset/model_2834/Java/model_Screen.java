





import java.util.List;
import java.util.ArrayList;

public class model_Screen extends NoteSupport, NameSupport, WidgetContainer {

    private String theme;
    private String minVersion;



    public model_Screen(
        String theme,        String minVersion    ) {
        super(
        );
        this.theme = theme;
        this.minVersion = minVersion;
    }


    public String getTheme() {
        return theme;
    }

    public void setTheme(String theme) {
        this.theme = theme;
    }
    public String getMinversion() {
        return minVersion;
    }

    public void setMinversion(String minVersion) {
        this.minVersion = minVersion;
    }


}