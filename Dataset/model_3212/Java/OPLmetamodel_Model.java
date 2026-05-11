





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_Model  {

    private String id;
    private boolean isConstraintProblem;





    private List<OPLmetamodel_Declaration> oplmetamodel_declarations;




    private List<OPLmetamodel_DataDeclaration> oplmetamodel_datadeclarations;




    private OPLmetamodel_SearchProcedure oplmetamodel_searchprocedure;




    private List<OPLmetamodel_DefinedType> oplmetamodel_definedtypes;




    private List<OPLmetamodel_Constraint> oplmetamodel_constraints;




    private List<OPLmetamodel_Script> oplmetamodel_scripts;




    private List<OPLmetamodel_ActivityDeclaration> oplmetamodel_activitydeclarations;




    private OPLmetamodel_Objective oplmetamodel_objective;




    private List<OPLmetamodel_Function> oplmetamodel_functions;




    private OPLmetamodel_ResourceDeclaration oplmetamodel_resourcedeclaration;




    private List<OPLmetamodel_ScheduleInitialization> oplmetamodel_scheduleinitializations;




    private List<OPLmetamodel_Setting> oplmetamodel_settings;




    private List<OPLmetamodel_Constraint> oplmetamodel_constraints;


    public OPLmetamodel_Model(
        String id,        boolean isConstraintProblem    ) {
        this.id = id;
        this.isConstraintProblem = isConstraintProblem;
        this.oplmetamodel_declarations = new ArrayList<>();
        this.oplmetamodel_datadeclarations = new ArrayList<>();
        this.oplmetamodel_definedtypes = new ArrayList<>();
        this.oplmetamodel_constraints = new ArrayList<>();
        this.oplmetamodel_scripts = new ArrayList<>();
        this.oplmetamodel_activitydeclarations = new ArrayList<>();
        this.oplmetamodel_functions = new ArrayList<>();
        this.oplmetamodel_scheduleinitializations = new ArrayList<>();
        this.oplmetamodel_settings = new ArrayList<>();
        this.oplmetamodel_constraints = new ArrayList<>();
    }

    public OPLmetamodel_Model(
        String id,        boolean isConstraintProblem        ArrayList<OPLmetamodel_Declaration> oplmetamodel_declarations,        ArrayList<OPLmetamodel_DataDeclaration> oplmetamodel_datadeclarations,        ArrayList<OPLmetamodel_DefinedType> oplmetamodel_definedtypes,        ArrayList<OPLmetamodel_Constraint> oplmetamodel_constraints,        ArrayList<OPLmetamodel_Script> oplmetamodel_scripts,        ArrayList<OPLmetamodel_ActivityDeclaration> oplmetamodel_activitydeclarations,        ArrayList<OPLmetamodel_Function> oplmetamodel_functions,        ArrayList<OPLmetamodel_ScheduleInitialization> oplmetamodel_scheduleinitializations,        ArrayList<OPLmetamodel_Setting> oplmetamodel_settings,        ArrayList<OPLmetamodel_Constraint> oplmetamodel_constraints    ) {
        this.id = id;
        this.isConstraintProblem = isConstraintProblem;
        this.oplmetamodel_declarations = oplmetamodel_declarations;
        this.oplmetamodel_datadeclarations = oplmetamodel_datadeclarations;
        this.oplmetamodel_definedtypes = oplmetamodel_definedtypes;
        this.oplmetamodel_constraints = oplmetamodel_constraints;
        this.oplmetamodel_scripts = oplmetamodel_scripts;
        this.oplmetamodel_activitydeclarations = oplmetamodel_activitydeclarations;
        this.oplmetamodel_functions = oplmetamodel_functions;
        this.oplmetamodel_scheduleinitializations = oplmetamodel_scheduleinitializations;
        this.oplmetamodel_settings = oplmetamodel_settings;
        this.oplmetamodel_constraints = oplmetamodel_constraints;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getIsconstraintproblem() {
        return isConstraintProblem;
    }

    public void setIsconstraintproblem(boolean isConstraintProblem) {
        this.isConstraintProblem = isConstraintProblem;
    }

    public List<OPLmetamodel_Declaration> getOplmetamodel_declarations() {
        return oplmetamodel_declarations;
    }

    public void addOplmetamodel_declaration(Oplmetamodel_declaration oplmetamodel_declaration) {
        this.oplmetamodel_declarations.add(oplmetamodel_declaration);
    }
    public List<OPLmetamodel_DataDeclaration> getOplmetamodel_datadeclarations() {
        return oplmetamodel_datadeclarations;
    }

    public void addOplmetamodel_datadeclaration(Oplmetamodel_datadeclaration oplmetamodel_datadeclaration) {
        this.oplmetamodel_datadeclarations.add(oplmetamodel_datadeclaration);
    }
    public OPLmetamodel_SearchProcedure getOplmetamodel_searchprocedure() {
        return oplmetamodel_searchprocedure;
    }

    public void setOplmetamodel_searchprocedure(OPLmetamodel_SearchProcedure oplmetamodel_searchprocedure) {
        this.oplmetamodel_searchprocedure = oplmetamodel_searchprocedure;
    }
    public List<OPLmetamodel_DefinedType> getOplmetamodel_definedtypes() {
        return oplmetamodel_definedtypes;
    }

    public void addOplmetamodel_definedtype(Oplmetamodel_definedtype oplmetamodel_definedtype) {
        this.oplmetamodel_definedtypes.add(oplmetamodel_definedtype);
    }
    public List<OPLmetamodel_Constraint> getOplmetamodel_constraints() {
        return oplmetamodel_constraints;
    }

    public void addOplmetamodel_constraint(Oplmetamodel_constraint oplmetamodel_constraint) {
        this.oplmetamodel_constraints.add(oplmetamodel_constraint);
    }
    public List<OPLmetamodel_Script> getOplmetamodel_scripts() {
        return oplmetamodel_scripts;
    }

    public void addOplmetamodel_script(Oplmetamodel_script oplmetamodel_script) {
        this.oplmetamodel_scripts.add(oplmetamodel_script);
    }
    public List<OPLmetamodel_ActivityDeclaration> getOplmetamodel_activitydeclarations() {
        return oplmetamodel_activitydeclarations;
    }

    public void addOplmetamodel_activitydeclaration(Oplmetamodel_activitydeclaration oplmetamodel_activitydeclaration) {
        this.oplmetamodel_activitydeclarations.add(oplmetamodel_activitydeclaration);
    }
    public OPLmetamodel_Objective getOplmetamodel_objective() {
        return oplmetamodel_objective;
    }

    public void setOplmetamodel_objective(OPLmetamodel_Objective oplmetamodel_objective) {
        this.oplmetamodel_objective = oplmetamodel_objective;
    }
    public List<OPLmetamodel_Function> getOplmetamodel_functions() {
        return oplmetamodel_functions;
    }

    public void addOplmetamodel_function(Oplmetamodel_function oplmetamodel_function) {
        this.oplmetamodel_functions.add(oplmetamodel_function);
    }
    public OPLmetamodel_ResourceDeclaration getOplmetamodel_resourcedeclaration() {
        return oplmetamodel_resourcedeclaration;
    }

    public void setOplmetamodel_resourcedeclaration(OPLmetamodel_ResourceDeclaration oplmetamodel_resourcedeclaration) {
        this.oplmetamodel_resourcedeclaration = oplmetamodel_resourcedeclaration;
    }
    public List<OPLmetamodel_ScheduleInitialization> getOplmetamodel_scheduleinitializations() {
        return oplmetamodel_scheduleinitializations;
    }

    public void addOplmetamodel_scheduleinitialization(Oplmetamodel_scheduleinitialization oplmetamodel_scheduleinitialization) {
        this.oplmetamodel_scheduleinitializations.add(oplmetamodel_scheduleinitialization);
    }
    public List<OPLmetamodel_Setting> getOplmetamodel_settings() {
        return oplmetamodel_settings;
    }

    public void addOplmetamodel_setting(Oplmetamodel_setting oplmetamodel_setting) {
        this.oplmetamodel_settings.add(oplmetamodel_setting);
    }
    public List<OPLmetamodel_Constraint> getOplmetamodel_constraints() {
        return oplmetamodel_constraints;
    }

    public void addOplmetamodel_constraint(Oplmetamodel_constraint oplmetamodel_constraint) {
        this.oplmetamodel_constraints.add(oplmetamodel_constraint);
    }

}