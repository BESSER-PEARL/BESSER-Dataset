





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Model  {






    private List<jpdl31_DocumentRoot> jpdl31_documentroots;


    public jpdl31_Model(
    ) {
        this.jpdl31_documentroots = new ArrayList<>();
    }

    public jpdl31_Model(
        ArrayList<jpdl31_DocumentRoot> jpdl31_documentroots    ) {
        this.jpdl31_documentroots = jpdl31_documentroots;
    }


    public List<jpdl31_DocumentRoot> getJpdl31_documentroots() {
        return jpdl31_documentroots;
    }

    public void addJpdl31_documentroot(Jpdl31_documentroot jpdl31_documentroot) {
        this.jpdl31_documentroots.add(jpdl31_documentroot);
    }

}