





import java.util.List;
import java.util.ArrayList;

public class model_Screen extends NoteSupport, WidgetContainer {

    private String name;
    private String theme;
    private String minVersion;



    public model_Screen(
        String name,        String theme,        String minVersion    ) {
        super(
        );
        this.name = name;
        this.theme = theme;
        this.minVersion = minVersion;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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