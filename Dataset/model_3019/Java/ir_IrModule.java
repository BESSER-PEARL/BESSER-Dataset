





import java.util.List;
import java.util.ArrayList;

public class ir_IrModule extends JobContainer {

    private String name;





    private List<ir_Variable> ir_variables;




    private List<ir_Connectivity> ir_connectivitys;




    private ir_SimpleVariable ir_simplevariable;




    private List<ir_SimpleVariable> ir_simplevariables;




    private ir_PostProcessingInfo ir_postprocessinginfo;




    private ir_ConnectivityVariable ir_connectivityvariable;




    private List<ir_ItemType> ir_itemtypes;




    private ir_SimpleVariable ir_simplevariable;




    private List<ir_Job> ir_jobs;




    private ir_ConnectivityVariable ir_connectivityvariable;




    private List<ir_Import> ir_imports;




    private ir_TimeLoop ir_timeloop;




    private List<ir_Function> ir_functions;


    public ir_IrModule(
        String name    ) {
        super(
        );
        this.name = name;
        this.ir_variables = new ArrayList<>();
        this.ir_connectivitys = new ArrayList<>();
        this.ir_simplevariables = new ArrayList<>();
        this.ir_itemtypes = new ArrayList<>();
        this.ir_jobs = new ArrayList<>();
        this.ir_imports = new ArrayList<>();
        this.ir_functions = new ArrayList<>();
    }

    public ir_IrModule(
        String name        ArrayList<ir_Variable> ir_variables,        ArrayList<ir_Connectivity> ir_connectivitys,        ArrayList<ir_SimpleVariable> ir_simplevariables,        ArrayList<ir_ItemType> ir_itemtypes,        ArrayList<ir_Job> ir_jobs,        ArrayList<ir_Import> ir_imports,        ArrayList<ir_Function> ir_functions    ) {
        this.name = name;
        this.ir_variables = ir_variables;
        this.ir_connectivitys = ir_connectivitys;
        this.ir_simplevariables = ir_simplevariables;
        this.ir_itemtypes = ir_itemtypes;
        this.ir_jobs = ir_jobs;
        this.ir_imports = ir_imports;
        this.ir_functions = ir_functions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ir_Variable> getIr_variables() {
        return ir_variables;
    }

    public void addIr_variable(Ir_variable ir_variable) {
        this.ir_variables.add(ir_variable);
    }
    public List<ir_Connectivity> getIr_connectivitys() {
        return ir_connectivitys;
    }

    public void addIr_connectivity(Ir_connectivity ir_connectivity) {
        this.ir_connectivitys.add(ir_connectivity);
    }
    public ir_SimpleVariable getIr_simplevariable() {
        return ir_simplevariable;
    }

    public void setIr_simplevariable(ir_SimpleVariable ir_simplevariable) {
        this.ir_simplevariable = ir_simplevariable;
    }
    public List<ir_SimpleVariable> getIr_simplevariables() {
        return ir_simplevariables;
    }

    public void addIr_simplevariable(Ir_simplevariable ir_simplevariable) {
        this.ir_simplevariables.add(ir_simplevariable);
    }
    public ir_PostProcessingInfo getIr_postprocessinginfo() {
        return ir_postprocessinginfo;
    }

    public void setIr_postprocessinginfo(ir_PostProcessingInfo ir_postprocessinginfo) {
        this.ir_postprocessinginfo = ir_postprocessinginfo;
    }
    public ir_ConnectivityVariable getIr_connectivityvariable() {
        return ir_connectivityvariable;
    }

    public void setIr_connectivityvariable(ir_ConnectivityVariable ir_connectivityvariable) {
        this.ir_connectivityvariable = ir_connectivityvariable;
    }
    public List<ir_ItemType> getIr_itemtypes() {
        return ir_itemtypes;
    }

    public void addIr_itemtype(Ir_itemtype ir_itemtype) {
        this.ir_itemtypes.add(ir_itemtype);
    }
    public ir_SimpleVariable getIr_simplevariable() {
        return ir_simplevariable;
    }

    public void setIr_simplevariable(ir_SimpleVariable ir_simplevariable) {
        this.ir_simplevariable = ir_simplevariable;
    }
    public List<ir_Job> getIr_jobs() {
        return ir_jobs;
    }

    public void addIr_job(Ir_job ir_job) {
        this.ir_jobs.add(ir_job);
    }
    public ir_ConnectivityVariable getIr_connectivityvariable() {
        return ir_connectivityvariable;
    }

    public void setIr_connectivityvariable(ir_ConnectivityVariable ir_connectivityvariable) {
        this.ir_connectivityvariable = ir_connectivityvariable;
    }
    public List<ir_Import> getIr_imports() {
        return ir_imports;
    }

    public void addIr_import(Ir_import ir_import) {
        this.ir_imports.add(ir_import);
    }
    public ir_TimeLoop getIr_timeloop() {
        return ir_timeloop;
    }

    public void setIr_timeloop(ir_TimeLoop ir_timeloop) {
        this.ir_timeloop = ir_timeloop;
    }
    public List<ir_Function> getIr_functions() {
        return ir_functions;
    }

    public void addIr_function(Ir_function ir_function) {
        this.ir_functions.add(ir_function);
    }

}