





import java.util.List;
import java.util.ArrayList;

public class SecCon_Project extends NamedElement {






    private List<SecCon_UseCaseScenario> seccon_usecasescenarios;




    private List<SecCon_Package> seccon_packages;




    private List<SecCon_StateMachineScenario> seccon_statemachinescenarios;


    public SecCon_Project(
    ) {
        super(
        );
        this.seccon_usecasescenarios = new ArrayList<>();
        this.seccon_packages = new ArrayList<>();
        this.seccon_statemachinescenarios = new ArrayList<>();
    }

    public SecCon_Project(
        ArrayList<SecCon_UseCaseScenario> seccon_usecasescenarios,        ArrayList<SecCon_Package> seccon_packages,        ArrayList<SecCon_StateMachineScenario> seccon_statemachinescenarios    ) {
        this.seccon_usecasescenarios = seccon_usecasescenarios;
        this.seccon_packages = seccon_packages;
        this.seccon_statemachinescenarios = seccon_statemachinescenarios;
    }


    public List<SecCon_UseCaseScenario> getSeccon_usecasescenarios() {
        return seccon_usecasescenarios;
    }

    public void addSeccon_usecasescenario(Seccon_usecasescenario seccon_usecasescenario) {
        this.seccon_usecasescenarios.add(seccon_usecasescenario);
    }
    public List<SecCon_Package> getSeccon_packages() {
        return seccon_packages;
    }

    public void addSeccon_package(Seccon_package seccon_package) {
        this.seccon_packages.add(seccon_package);
    }
    public List<SecCon_StateMachineScenario> getSeccon_statemachinescenarios() {
        return seccon_statemachinescenarios;
    }

    public void addSeccon_statemachinescenario(Seccon_statemachinescenario seccon_statemachinescenario) {
        this.seccon_statemachinescenarios.add(seccon_statemachinescenario);
    }

}