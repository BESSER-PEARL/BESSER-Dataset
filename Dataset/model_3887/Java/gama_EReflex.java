





import java.util.List;
import java.util.ArrayList;

public class gama_EReflex extends EGamaObject {

    private String gamlCode;





    private gama_EReflexLink gama_ereflexlink;




    private List<gama_EReflexLink> gama_ereflexlinks;


    public gama_EReflex(
        String gamlCode    ) {
        super(
        );
        this.gamlCode = gamlCode;
        this.gama_ereflexlinks = new ArrayList<>();
    }

    public gama_EReflex(
        String gamlCode        ArrayList<gama_EReflexLink> gama_ereflexlinks    ) {
        this.gamlCode = gamlCode;
        this.gama_ereflexlinks = gama_ereflexlinks;
    }

    public String getGamlcode() {
        return gamlCode;
    }

    public void setGamlcode(String gamlCode) {
        this.gamlCode = gamlCode;
    }

    public gama_EReflexLink getGama_ereflexlink() {
        return gama_ereflexlink;
    }

    public void setGama_ereflexlink(gama_EReflexLink gama_ereflexlink) {
        this.gama_ereflexlink = gama_ereflexlink;
    }
    public List<gama_EReflexLink> getGama_ereflexlinks() {
        return gama_ereflexlinks;
    }

    public void addGama_ereflexlink(Gama_ereflexlink gama_ereflexlink) {
        this.gama_ereflexlinks.add(gama_ereflexlink);
    }

}