





import java.util.List;
import java.util.ArrayList;

public class camel_organisation_CloudProvider extends Organisation {

    private boolean SaaS;
    private boolean IaaS;
    private boolean public;
    private boolean PaaS;





    private ProviderModel providermodel;


    public camel_organisation_CloudProvider(
        boolean SaaS,        boolean IaaS,        boolean public,        boolean PaaS    ) {
        super(
        );
        this.SaaS = SaaS;
        this.IaaS = IaaS;
        this.public = public;
        this.PaaS = PaaS;
    }


    public boolean getSaas() {
        return SaaS;
    }

    public void setSaas(boolean SaaS) {
        this.SaaS = SaaS;
    }
    public boolean getIaas() {
        return IaaS;
    }

    public void setIaas(boolean IaaS) {
        this.IaaS = IaaS;
    }
    public boolean getPublic() {
        return public;
    }

    public void setPublic(boolean public) {
        this.public = public;
    }
    public boolean getPaas() {
        return PaaS;
    }

    public void setPaas(boolean PaaS) {
        this.PaaS = PaaS;
    }

    public ProviderModel getProvidermodel() {
        return providermodel;
    }

    public void setProvidermodel(ProviderModel providermodel) {
        this.providermodel = providermodel;
    }

}