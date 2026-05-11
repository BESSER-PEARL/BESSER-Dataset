





import java.util.List;
import java.util.ArrayList;

public class camel_CamelModel extends Model {






    private List<SecurityModel> securitymodels;




    private List<ProviderModel> providermodels;




    private List<TypeModel> typemodels;




    private List<RequirementModel> requirementmodels;




    private List<ScalabilityModel> scalabilitymodels;


    public camel_CamelModel(
    ) {
        super(
        );
        this.securitymodels = new ArrayList<>();
        this.providermodels = new ArrayList<>();
        this.typemodels = new ArrayList<>();
        this.requirementmodels = new ArrayList<>();
        this.scalabilitymodels = new ArrayList<>();
    }

    public camel_CamelModel(
        ArrayList<SecurityModel> securitymodels,        ArrayList<ProviderModel> providermodels,        ArrayList<TypeModel> typemodels,        ArrayList<RequirementModel> requirementmodels,        ArrayList<ScalabilityModel> scalabilitymodels    ) {
        this.securitymodels = securitymodels;
        this.providermodels = providermodels;
        this.typemodels = typemodels;
        this.requirementmodels = requirementmodels;
        this.scalabilitymodels = scalabilitymodels;
    }


    public List<SecurityModel> getSecuritymodels() {
        return securitymodels;
    }

    public void addSecuritymodel(Securitymodel securitymodel) {
        this.securitymodels.add(securitymodel);
    }
    public List<ProviderModel> getProvidermodels() {
        return providermodels;
    }

    public void addProvidermodel(Providermodel providermodel) {
        this.providermodels.add(providermodel);
    }
    public List<TypeModel> getTypemodels() {
        return typemodels;
    }

    public void addTypemodel(Typemodel typemodel) {
        this.typemodels.add(typemodel);
    }
    public List<RequirementModel> getRequirementmodels() {
        return requirementmodels;
    }

    public void addRequirementmodel(Requirementmodel requirementmodel) {
        this.requirementmodels.add(requirementmodel);
    }
    public List<ScalabilityModel> getScalabilitymodels() {
        return scalabilitymodels;
    }

    public void addScalabilitymodel(Scalabilitymodel scalabilitymodel) {
        this.scalabilitymodels.add(scalabilitymodel);
    }

}