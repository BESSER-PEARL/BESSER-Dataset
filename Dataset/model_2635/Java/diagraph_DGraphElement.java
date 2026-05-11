





import java.util.List;
import java.util.ArrayList;

public class diagraph_DGraphElement  {

    private boolean abztract;
    private String icon;
    private String name;



    public diagraph_DGraphElement(
        boolean abztract,        String icon,        String name    ) {
        this.abztract = abztract;
        this.icon = icon;
        this.name = name;
    }


    public boolean getAbztract() {
        return abztract;
    }

    public void setAbztract(boolean abztract) {
        this.abztract = abztract;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}