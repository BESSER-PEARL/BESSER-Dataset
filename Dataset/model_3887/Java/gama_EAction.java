





import java.util.List;
import java.util.ArrayList;

public class gama_EAction extends EGamaObject {

    private String gamlCode;
    private String returnType;





    private gama_EActionLink gama_eactionlink;




    private List<gama_EActionLink> gama_eactionlinks;




    private List<gama_EVariable> gama_evariables;


    public gama_EAction(
        String gamlCode,        String returnType    ) {
        super(
        );
        this.gamlCode = gamlCode;
        this.returnType = returnType;
        this.gama_eactionlinks = new ArrayList<>();
        this.gama_evariables = new ArrayList<>();
    }

    public gama_EAction(
        String gamlCode,        String returnType        ArrayList<gama_EActionLink> gama_eactionlinks,        ArrayList<gama_EVariable> gama_evariables    ) {
        this.gamlCode = gamlCode;
        this.returnType = returnType;
        this.gama_eactionlinks = gama_eactionlinks;
        this.gama_evariables = gama_evariables;
    }

    public String getGamlcode() {
        return gamlCode;
    }

    public void setGamlcode(String gamlCode) {
        this.gamlCode = gamlCode;
    }
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }

    public gama_EActionLink getGama_eactionlink() {
        return gama_eactionlink;
    }

    public void setGama_eactionlink(gama_EActionLink gama_eactionlink) {
        this.gama_eactionlink = gama_eactionlink;
    }
    public List<gama_EActionLink> getGama_eactionlinks() {
        return gama_eactionlinks;
    }

    public void addGama_eactionlink(Gama_eactionlink gama_eactionlink) {
        this.gama_eactionlinks.add(gama_eactionlink);
    }
    public List<gama_EVariable> getGama_evariables() {
        return gama_evariables;
    }

    public void addGama_evariable(Gama_evariable gama_evariable) {
        this.gama_evariables.add(gama_evariable);
    }

}