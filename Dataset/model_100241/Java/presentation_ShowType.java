





import java.util.List;
import java.util.ArrayList;

public class presentation_ShowType  {

    private String pages;
    private String name;





    private presentation_SettingsType presentation_settingstype;


    public presentation_ShowType(
        String pages,        String name    ) {
        this.pages = pages;
        this.name = name;
    }


    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public presentation_SettingsType getPresentation_settingstype() {
        return presentation_settingstype;
    }

    public void setPresentation_settingstype(presentation_SettingsType presentation_settingstype) {
        this.presentation_settingstype = presentation_settingstype;
    }

}