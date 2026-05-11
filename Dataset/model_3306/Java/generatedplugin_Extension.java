





import java.util.List;
import java.util.ArrayList;

public class generatedplugin_Extension  {

    private String point;





    private List<generatedplugin_DublinCore> generatedplugin_dublincores;




    private generatedplugin_Plugin generatedplugin_plugin;


    public generatedplugin_Extension(
        String point    ) {
        this.point = point;
        this.generatedplugin_dublincores = new ArrayList<>();
    }

    public generatedplugin_Extension(
        String point        ArrayList<generatedplugin_DublinCore> generatedplugin_dublincores    ) {
        this.point = point;
        this.generatedplugin_dublincores = generatedplugin_dublincores;
    }

    public String getPoint() {
        return point;
    }

    public void setPoint(String point) {
        this.point = point;
    }

    public List<generatedplugin_DublinCore> getGeneratedplugin_dublincores() {
        return generatedplugin_dublincores;
    }

    public void addGeneratedplugin_dublincore(Generatedplugin_dublincore generatedplugin_dublincore) {
        this.generatedplugin_dublincores.add(generatedplugin_dublincore);
    }
    public generatedplugin_Plugin getGeneratedplugin_plugin() {
        return generatedplugin_plugin;
    }

    public void setGeneratedplugin_plugin(generatedplugin_Plugin generatedplugin_plugin) {
        this.generatedplugin_plugin = generatedplugin_plugin;
    }

}