





import java.util.List;
import java.util.ArrayList;

public class ProviderSystem_Provider  {

    private String name;
    private int pricePerUnit;





    private List<ProviderSystem_Consomation> providersystem_consomations;




    private List<ProviderSystem_Fuel> providersystem_fuels;


    public ProviderSystem_Provider(
        String name,        int pricePerUnit    ) {
        this.name = name;
        this.pricePerUnit = pricePerUnit;
        this.providersystem_consomations = new ArrayList<>();
        this.providersystem_fuels = new ArrayList<>();
    }

    public ProviderSystem_Provider(
        String name,        int pricePerUnit        ArrayList<ProviderSystem_Consomation> providersystem_consomations,        ArrayList<ProviderSystem_Fuel> providersystem_fuels    ) {
        this.name = name;
        this.pricePerUnit = pricePerUnit;
        this.providersystem_consomations = providersystem_consomations;
        this.providersystem_fuels = providersystem_fuels;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPriceperunit() {
        return pricePerUnit;
    }

    public void setPriceperunit(int pricePerUnit) {
        this.pricePerUnit = pricePerUnit;
    }

    public List<ProviderSystem_Consomation> getProvidersystem_consomations() {
        return providersystem_consomations;
    }

    public void addProvidersystem_consomation(Providersystem_consomation providersystem_consomation) {
        this.providersystem_consomations.add(providersystem_consomation);
    }
    public List<ProviderSystem_Fuel> getProvidersystem_fuels() {
        return providersystem_fuels;
    }

    public void addProvidersystem_fuel(Providersystem_fuel providersystem_fuel) {
        this.providersystem_fuels.add(providersystem_fuel);
    }

}