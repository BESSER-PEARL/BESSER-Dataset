





import java.util.List;
import java.util.ArrayList;

public class archimateC2_Product extends PassiveStructure {

    private String contract;





    private List<archimateC2_Contract> archimatec2_contracts;




    private List<archimateC2_ApplicationService> archimatec2_applicationservices;




    private archimateC2_BusinessService archimatec2_businessservice;




    private archimateC2_Contract archimatec2_contract;




    private List<archimateC2_Value> archimatec2_values;




    private archimateC2_Value archimatec2_value;




    private List<archimateC2_BusinessService> archimatec2_businessservices;




    private List<archimateC2_InfrastructureService> archimatec2_infrastructureservices;




    private archimateC2_ApplicationService archimatec2_applicationservice;




    private archimateC2_InfrastructureService archimatec2_infrastructureservice;


    public archimateC2_Product(
        String contract    ) {
        super(
        );
        this.contract = contract;
        this.archimatec2_contracts = new ArrayList<>();
        this.archimatec2_applicationservices = new ArrayList<>();
        this.archimatec2_values = new ArrayList<>();
        this.archimatec2_businessservices = new ArrayList<>();
        this.archimatec2_infrastructureservices = new ArrayList<>();
    }

    public archimateC2_Product(
        String contract        ArrayList<archimateC2_Contract> archimatec2_contracts,        ArrayList<archimateC2_ApplicationService> archimatec2_applicationservices,        ArrayList<archimateC2_Value> archimatec2_values,        ArrayList<archimateC2_BusinessService> archimatec2_businessservices,        ArrayList<archimateC2_InfrastructureService> archimatec2_infrastructureservices    ) {
        this.contract = contract;
        this.archimatec2_contracts = archimatec2_contracts;
        this.archimatec2_applicationservices = archimatec2_applicationservices;
        this.archimatec2_values = archimatec2_values;
        this.archimatec2_businessservices = archimatec2_businessservices;
        this.archimatec2_infrastructureservices = archimatec2_infrastructureservices;
    }

    public String getContract() {
        return contract;
    }

    public void setContract(String contract) {
        this.contract = contract;
    }

    public List<archimateC2_Contract> getArchimatec2_contracts() {
        return archimatec2_contracts;
    }

    public void addArchimatec2_contract(Archimatec2_contract archimatec2_contract) {
        this.archimatec2_contracts.add(archimatec2_contract);
    }
    public List<archimateC2_ApplicationService> getArchimatec2_applicationservices() {
        return archimatec2_applicationservices;
    }

    public void addArchimatec2_applicationservice(Archimatec2_applicationservice archimatec2_applicationservice) {
        this.archimatec2_applicationservices.add(archimatec2_applicationservice);
    }
    public archimateC2_BusinessService getArchimatec2_businessservice() {
        return archimatec2_businessservice;
    }

    public void setArchimatec2_businessservice(archimateC2_BusinessService archimatec2_businessservice) {
        this.archimatec2_businessservice = archimatec2_businessservice;
    }
    public archimateC2_Contract getArchimatec2_contract() {
        return archimatec2_contract;
    }

    public void setArchimatec2_contract(archimateC2_Contract archimatec2_contract) {
        this.archimatec2_contract = archimatec2_contract;
    }
    public List<archimateC2_Value> getArchimatec2_values() {
        return archimatec2_values;
    }

    public void addArchimatec2_value(Archimatec2_value archimatec2_value) {
        this.archimatec2_values.add(archimatec2_value);
    }
    public archimateC2_Value getArchimatec2_value() {
        return archimatec2_value;
    }

    public void setArchimatec2_value(archimateC2_Value archimatec2_value) {
        this.archimatec2_value = archimatec2_value;
    }
    public List<archimateC2_BusinessService> getArchimatec2_businessservices() {
        return archimatec2_businessservices;
    }

    public void addArchimatec2_businessservice(Archimatec2_businessservice archimatec2_businessservice) {
        this.archimatec2_businessservices.add(archimatec2_businessservice);
    }
    public List<archimateC2_InfrastructureService> getArchimatec2_infrastructureservices() {
        return archimatec2_infrastructureservices;
    }

    public void addArchimatec2_infrastructureservice(Archimatec2_infrastructureservice archimatec2_infrastructureservice) {
        this.archimatec2_infrastructureservices.add(archimatec2_infrastructureservice);
    }
    public archimateC2_ApplicationService getArchimatec2_applicationservice() {
        return archimatec2_applicationservice;
    }

    public void setArchimatec2_applicationservice(archimateC2_ApplicationService archimatec2_applicationservice) {
        this.archimatec2_applicationservice = archimatec2_applicationservice;
    }
    public archimateC2_InfrastructureService getArchimatec2_infrastructureservice() {
        return archimatec2_infrastructureservice;
    }

    public void setArchimatec2_infrastructureservice(archimateC2_InfrastructureService archimatec2_infrastructureservice) {
        this.archimatec2_infrastructureservice = archimatec2_infrastructureservice;
    }

}