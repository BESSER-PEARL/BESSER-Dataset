





import java.util.List;
import java.util.ArrayList;

public class avm_TestBench  {

    private String Name;





    private List<avm_DomainModel_> avm_domainmodel_s;




    private List<avm_ComponentInstance> avm_componentinstances;


    public avm_TestBench(
        String Name    ) {
        this.Name = Name;
        this.avm_domainmodel_s = new ArrayList<>();
        this.avm_componentinstances = new ArrayList<>();
    }

    public avm_TestBench(
        String Name        ArrayList<avm_DomainModel_> avm_domainmodel_s,        ArrayList<avm_ComponentInstance> avm_componentinstances    ) {
        this.Name = Name;
        this.avm_domainmodel_s = avm_domainmodel_s;
        this.avm_componentinstances = avm_componentinstances;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<avm_DomainModel_> getAvm_domainmodel_s() {
        return avm_domainmodel_s;
    }

    public void addAvm_domainmodel_(Avm_domainmodel_ avm_domainmodel_) {
        this.avm_domainmodel_s.add(avm_domainmodel_);
    }
    public List<avm_ComponentInstance> getAvm_componentinstances() {
        return avm_componentinstances;
    }

    public void addAvm_componentinstance(Avm_componentinstance avm_componentinstance) {
        this.avm_componentinstances.add(avm_componentinstance);
    }

}