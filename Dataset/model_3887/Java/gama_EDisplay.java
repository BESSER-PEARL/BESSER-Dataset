





import java.util.List;
import java.util.ArrayList;

public class gama_EDisplay extends EGamaObject {

    private boolean defineGamlCode;
    private String layerList;
    private String gamlCode;



    public gama_EDisplay(
        boolean defineGamlCode,        String layerList,        String gamlCode    ) {
        super(
        );
        this.defineGamlCode = defineGamlCode;
        this.layerList = layerList;
        this.gamlCode = gamlCode;
    }


    public boolean getDefinegamlcode() {
        return defineGamlCode;
    }

    public void setDefinegamlcode(boolean defineGamlCode) {
        this.defineGamlCode = defineGamlCode;
    }
    public String getLayerlist() {
        return layerList;
    }

    public void setLayerlist(String layerList) {
        this.layerList = layerList;
    }
    public String getGamlcode() {
        return gamlCode;
    }

    public void setGamlcode(String gamlCode) {
        this.gamlCode = gamlCode;
    }


}