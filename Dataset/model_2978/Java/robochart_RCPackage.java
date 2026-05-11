





import java.util.List;
import java.util.ArrayList;

public class robochart_RCPackage extends BasicPackage {






    private List<robochart_TypeDecl> robochart_typedecls;




    private List<robochart_RCModule> robochart_rcmodules;




    private List<robochart_StateMachineDef> robochart_statemachinedefs;




    private List<robochart_OperationDef> robochart_operationdefs;




    private List<robochart_RoboticPlatformDef> robochart_roboticplatformdefs;




    private List<robochart_Interface> robochart_interfaces;




    private List<robochart_ControllerDef> robochart_controllerdefs;




    private List<robochart_Function> robochart_functions;


    public robochart_RCPackage(
    ) {
        super(
        );
        this.robochart_typedecls = new ArrayList<>();
        this.robochart_rcmodules = new ArrayList<>();
        this.robochart_statemachinedefs = new ArrayList<>();
        this.robochart_operationdefs = new ArrayList<>();
        this.robochart_roboticplatformdefs = new ArrayList<>();
        this.robochart_interfaces = new ArrayList<>();
        this.robochart_controllerdefs = new ArrayList<>();
        this.robochart_functions = new ArrayList<>();
    }

    public robochart_RCPackage(
        ArrayList<robochart_TypeDecl> robochart_typedecls,        ArrayList<robochart_RCModule> robochart_rcmodules,        ArrayList<robochart_StateMachineDef> robochart_statemachinedefs,        ArrayList<robochart_OperationDef> robochart_operationdefs,        ArrayList<robochart_RoboticPlatformDef> robochart_roboticplatformdefs,        ArrayList<robochart_Interface> robochart_interfaces,        ArrayList<robochart_ControllerDef> robochart_controllerdefs,        ArrayList<robochart_Function> robochart_functions    ) {
        this.robochart_typedecls = robochart_typedecls;
        this.robochart_rcmodules = robochart_rcmodules;
        this.robochart_statemachinedefs = robochart_statemachinedefs;
        this.robochart_operationdefs = robochart_operationdefs;
        this.robochart_roboticplatformdefs = robochart_roboticplatformdefs;
        this.robochart_interfaces = robochart_interfaces;
        this.robochart_controllerdefs = robochart_controllerdefs;
        this.robochart_functions = robochart_functions;
    }


    public List<robochart_TypeDecl> getRobochart_typedecls() {
        return robochart_typedecls;
    }

    public void addRobochart_typedecl(Robochart_typedecl robochart_typedecl) {
        this.robochart_typedecls.add(robochart_typedecl);
    }
    public List<robochart_RCModule> getRobochart_rcmodules() {
        return robochart_rcmodules;
    }

    public void addRobochart_rcmodule(Robochart_rcmodule robochart_rcmodule) {
        this.robochart_rcmodules.add(robochart_rcmodule);
    }
    public List<robochart_StateMachineDef> getRobochart_statemachinedefs() {
        return robochart_statemachinedefs;
    }

    public void addRobochart_statemachinedef(Robochart_statemachinedef robochart_statemachinedef) {
        this.robochart_statemachinedefs.add(robochart_statemachinedef);
    }
    public List<robochart_OperationDef> getRobochart_operationdefs() {
        return robochart_operationdefs;
    }

    public void addRobochart_operationdef(Robochart_operationdef robochart_operationdef) {
        this.robochart_operationdefs.add(robochart_operationdef);
    }
    public List<robochart_RoboticPlatformDef> getRobochart_roboticplatformdefs() {
        return robochart_roboticplatformdefs;
    }

    public void addRobochart_roboticplatformdef(Robochart_roboticplatformdef robochart_roboticplatformdef) {
        this.robochart_roboticplatformdefs.add(robochart_roboticplatformdef);
    }
    public List<robochart_Interface> getRobochart_interfaces() {
        return robochart_interfaces;
    }

    public void addRobochart_interface(Robochart_interface robochart_interface) {
        this.robochart_interfaces.add(robochart_interface);
    }
    public List<robochart_ControllerDef> getRobochart_controllerdefs() {
        return robochart_controllerdefs;
    }

    public void addRobochart_controllerdef(Robochart_controllerdef robochart_controllerdef) {
        this.robochart_controllerdefs.add(robochart_controllerdef);
    }
    public List<robochart_Function> getRobochart_functions() {
        return robochart_functions;
    }

    public void addRobochart_function(Robochart_function robochart_function) {
        this.robochart_functions.add(robochart_function);
    }

}