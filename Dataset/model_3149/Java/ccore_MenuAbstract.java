





import java.util.List;
import java.util.ArrayList;

public class ccore_MenuAbstract  {

    private String icon;
    private String path;
    private String label;





    private ccore_Menu ccore_menu;


    public ccore_MenuAbstract(
        String icon,        String path,        String label    ) {
        this.icon = icon;
        this.path = path;
        this.label = label;
    }


    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public ccore_Menu getCcore_menu() {
        return ccore_menu;
    }

    public void setCcore_menu(ccore_Menu ccore_menu) {
        this.ccore_menu = ccore_menu;
    }

}