





import java.util.List;
import java.util.ArrayList;

public class diagraph_DGraphElement  {

    private String icon;
    private boolean abztract;
    private String name;



    public diagraph_DGraphElement(
        String icon,        boolean abztract,        String name    ) {
        this.icon = icon;
        this.abztract = abztract;
        this.name = name;
    }


    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public boolean getAbztract() {
        return abztract;
    }

    public void setAbztract(boolean abztract) {
        this.abztract = abztract;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}