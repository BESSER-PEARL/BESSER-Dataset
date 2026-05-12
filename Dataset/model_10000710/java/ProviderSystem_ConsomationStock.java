





import java.util.List;
import java.util.ArrayList;

public class ProviderSystem_ConsomationStock  {

    private int _capacity;





    private List<ProviderSystem_Consomation> providersystem_consomations;


    public ProviderSystem_ConsomationStock(
        int _capacity    ) {
        this._capacity = _capacity;
        this.providersystem_consomations = new ArrayList<>();
    }

    public ProviderSystem_ConsomationStock(
        int _capacity        ArrayList<ProviderSystem_Consomation> providersystem_consomations    ) {
        this._capacity = _capacity;
        this.providersystem_consomations = providersystem_consomations;
    }

    public int get_capacity() {
        return _capacity;
    }

    public void set_capacity(int _capacity) {
        this._capacity = _capacity;
    }

    public List<ProviderSystem_Consomation> getProvidersystem_consomations() {
        return providersystem_consomations;
    }

    public void addProvidersystem_consomation(Providersystem_consomation providersystem_consomation) {
        this.providersystem_consomations.add(providersystem_consomation);
    }

}