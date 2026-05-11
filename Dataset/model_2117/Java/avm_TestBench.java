





import java.util.List;
import java.util.ArrayList;

public class avm_TestBench  {

    private String Name;





    private List<avm_DomainModel_> avm_domainmodel_s;




    private List<avm_Metric> avm_metrics;




    private List<avm_Parameter> avm_parameters;




    private List<avm_ComponentInstance> avm_componentinstances;




    private List<avm_TestInjectionPoint> avm_testinjectionpoints;


    public avm_TestBench(
        String Name    ) {
        this.Name = Name;
        this.avm_domainmodel_s = new ArrayList<>();
        this.avm_metrics = new ArrayList<>();
        this.avm_parameters = new ArrayList<>();
        this.avm_componentinstances = new ArrayList<>();
        this.avm_testinjectionpoints = new ArrayList<>();
    }

    public avm_TestBench(
        String Name        ArrayList<avm_DomainModel_> avm_domainmodel_s,        ArrayList<avm_Metric> avm_metrics,        ArrayList<avm_Parameter> avm_parameters,        ArrayList<avm_ComponentInstance> avm_componentinstances,        ArrayList<avm_TestInjectionPoint> avm_testinjectionpoints    ) {
        this.Name = Name;
        this.avm_domainmodel_s = avm_domainmodel_s;
        this.avm_metrics = avm_metrics;
        this.avm_parameters = avm_parameters;
        this.avm_componentinstances = avm_componentinstances;
        this.avm_testinjectionpoints = avm_testinjectionpoints;
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
    public List<avm_Metric> getAvm_metrics() {
        return avm_metrics;
    }

    public void addAvm_metric(Avm_metric avm_metric) {
        this.avm_metrics.add(avm_metric);
    }
    public List<avm_Parameter> getAvm_parameters() {
        return avm_parameters;
    }

    public void addAvm_parameter(Avm_parameter avm_parameter) {
        this.avm_parameters.add(avm_parameter);
    }
    public List<avm_ComponentInstance> getAvm_componentinstances() {
        return avm_componentinstances;
    }

    public void addAvm_componentinstance(Avm_componentinstance avm_componentinstance) {
        this.avm_componentinstances.add(avm_componentinstance);
    }
    public List<avm_TestInjectionPoint> getAvm_testinjectionpoints() {
        return avm_testinjectionpoints;
    }

    public void addAvm_testinjectionpoint(Avm_testinjectionpoint avm_testinjectionpoint) {
        this.avm_testinjectionpoints.add(avm_testinjectionpoint);
    }

}