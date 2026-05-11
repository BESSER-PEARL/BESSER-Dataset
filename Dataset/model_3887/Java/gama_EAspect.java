





import java.util.List;
import java.util.ArrayList;

public class gama_EAspect extends EGamaObject {

    private boolean defineGamlCode;
    private String gamlCode;





    private List<gama_EAspectLink> gama_easpectlinks;




    private List<gama_ELayerAspect> gama_elayeraspects;




    private gama_EAspectLink gama_easpectlink;




    private gama_ELayerAspect gama_elayeraspect;


    public gama_EAspect(
        boolean defineGamlCode,        String gamlCode    ) {
        super(
        );
        this.defineGamlCode = defineGamlCode;
        this.gamlCode = gamlCode;
        this.gama_easpectlinks = new ArrayList<>();
        this.gama_elayeraspects = new ArrayList<>();
    }

    public gama_EAspect(
        boolean defineGamlCode,        String gamlCode        ArrayList<gama_EAspectLink> gama_easpectlinks,        ArrayList<gama_ELayerAspect> gama_elayeraspects    ) {
        this.defineGamlCode = defineGamlCode;
        this.gamlCode = gamlCode;
        this.gama_easpectlinks = gama_easpectlinks;
        this.gama_elayeraspects = gama_elayeraspects;
    }

    public boolean getDefinegamlcode() {
        return defineGamlCode;
    }

    public void setDefinegamlcode(boolean defineGamlCode) {
        this.defineGamlCode = defineGamlCode;
    }
    public String getGamlcode() {
        return gamlCode;
    }

    public void setGamlcode(String gamlCode) {
        this.gamlCode = gamlCode;
    }

    public List<gama_EAspectLink> getGama_easpectlinks() {
        return gama_easpectlinks;
    }

    public void addGama_easpectlink(Gama_easpectlink gama_easpectlink) {
        this.gama_easpectlinks.add(gama_easpectlink);
    }
    public List<gama_ELayerAspect> getGama_elayeraspects() {
        return gama_elayeraspects;
    }

    public void addGama_elayeraspect(Gama_elayeraspect gama_elayeraspect) {
        this.gama_elayeraspects.add(gama_elayeraspect);
    }
    public gama_EAspectLink getGama_easpectlink() {
        return gama_easpectlink;
    }

    public void setGama_easpectlink(gama_EAspectLink gama_easpectlink) {
        this.gama_easpectlink = gama_easpectlink;
    }
    public gama_ELayerAspect getGama_elayeraspect() {
        return gama_elayeraspect;
    }

    public void setGama_elayeraspect(gama_ELayerAspect gama_elayeraspect) {
        this.gama_elayeraspect = gama_elayeraspect;
    }

}