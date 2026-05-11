





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Reference_Monitor  {






    private ioT_metamodel_Policy_Repository iot_metamodel_policy_repository;




    private List<ioT_metamodel_Authorizor> iot_metamodel_authorizors;




    private ioT_metamodel_Policy_Repository iot_metamodel_policy_repository;


    public ioT_metamodel_Reference_Monitor(
    ) {
        this.iot_metamodel_authorizors = new ArrayList<>();
    }

    public ioT_metamodel_Reference_Monitor(
        ArrayList<ioT_metamodel_Authorizor> iot_metamodel_authorizors    ) {
        this.iot_metamodel_authorizors = iot_metamodel_authorizors;
    }


    public ioT_metamodel_Policy_Repository getIot_metamodel_policy_repository() {
        return iot_metamodel_policy_repository;
    }

    public void setIot_metamodel_policy_repository(ioT_metamodel_Policy_Repository iot_metamodel_policy_repository) {
        this.iot_metamodel_policy_repository = iot_metamodel_policy_repository;
    }
    public List<ioT_metamodel_Authorizor> getIot_metamodel_authorizors() {
        return iot_metamodel_authorizors;
    }

    public void addIot_metamodel_authorizor(Iot_metamodel_authorizor iot_metamodel_authorizor) {
        this.iot_metamodel_authorizors.add(iot_metamodel_authorizor);
    }
    public ioT_metamodel_Policy_Repository getIot_metamodel_policy_repository() {
        return iot_metamodel_policy_repository;
    }

    public void setIot_metamodel_policy_repository(ioT_metamodel_Policy_Repository iot_metamodel_policy_repository) {
        this.iot_metamodel_policy_repository = iot_metamodel_policy_repository;
    }

}