





import java.util.List;
import java.util.ArrayList;

public class model_Screen extends NoteSupport, WidgetContainer {

    private String minVersion;
    private String name;
    private String theme;



    public model_Screen(
        String minVersion,        String name,        String theme    ) {
        super(
        );
        this.minVersion = minVersion;
        this.name = name;
        this.theme = theme;
    }


    public String getMinversion() {
        return minVersion;
    }

    public void setMinversion(String minVersion) {
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


}