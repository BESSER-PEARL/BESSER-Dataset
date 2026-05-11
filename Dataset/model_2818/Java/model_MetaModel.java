





import java.util.List;
import java.util.ArrayList;

public class model_MetaModel  {

    private String ecorePath;
    private String plugin;





    private model_XDiagram model_xdiagram;


    public model_MetaModel(
        String ecorePath,        String plugin    ) {
        this.ecorePath = ecorePath;
        this.plugin = plugin;
    }


    public String getEcorepath() {
        return ecorePath;
    }

    public void setEcorepath(String ecorePath) {
        this.ecorePath = ecorePath;
    }
    public String getPlugin() {
        return plugin;
    }

    public void setPlugin(String plugin) {
        this.plugin = plugin;
    }

    public model_XDiagram getModel_xdiagram() {
        return model_xdiagram;
    }

    public void setModel_xdiagram(model_XDiagram model_xdiagram) {
        this.model_xdiagram = model_xdiagram;
    }

}