





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_Workbench  {






    private List<effbdpattern_Context> effbdpattern_contexts;




    private effbdpattern_PatternCatalog effbdpattern_patterncatalog;




    private List<effbdpattern_Condition> effbdpattern_conditions;




    private List<effbdpattern_Domain> effbdpattern_domains;




    private List<effbdpattern_Allocation> effbdpattern_allocations;




    private List<effbdpattern_Feature> effbdpattern_features;




    private List<effbdpattern_Problem> effbdpattern_problems;




    private List<effbdpattern_FunctionProperty> effbdpattern_functionpropertys;




    private List<effbdpattern_Model> effbdpattern_models;


    public effbdpattern_Workbench(
    ) {
        this.effbdpattern_contexts = new ArrayList<>();
        this.effbdpattern_conditions = new ArrayList<>();
        this.effbdpattern_domains = new ArrayList<>();
        this.effbdpattern_allocations = new ArrayList<>();
        this.effbdpattern_features = new ArrayList<>();
        this.effbdpattern_problems = new ArrayList<>();
        this.effbdpattern_functionpropertys = new ArrayList<>();
        this.effbdpattern_models = new ArrayList<>();
    }

    public effbdpattern_Workbench(
        ArrayList<effbdpattern_Context> effbdpattern_contexts,        ArrayList<effbdpattern_Condition> effbdpattern_conditions,        ArrayList<effbdpattern_Domain> effbdpattern_domains,        ArrayList<effbdpattern_Allocation> effbdpattern_allocations,        ArrayList<effbdpattern_Feature> effbdpattern_features,        ArrayList<effbdpattern_Problem> effbdpattern_problems,        ArrayList<effbdpattern_FunctionProperty> effbdpattern_functionpropertys,        ArrayList<effbdpattern_Model> effbdpattern_models    ) {
        this.effbdpattern_contexts = effbdpattern_contexts;
        this.effbdpattern_conditions = effbdpattern_conditions;
        this.effbdpattern_domains = effbdpattern_domains;
        this.effbdpattern_allocations = effbdpattern_allocations;
        this.effbdpattern_features = effbdpattern_features;
        this.effbdpattern_problems = effbdpattern_problems;
        this.effbdpattern_functionpropertys = effbdpattern_functionpropertys;
        this.effbdpattern_models = effbdpattern_models;
    }


    public List<effbdpattern_Context> getEffbdpattern_contexts() {
        return effbdpattern_contexts;
    }

    public void addEffbdpattern_context(Effbdpattern_context effbdpattern_context) {
        this.effbdpattern_contexts.add(effbdpattern_context);
    }
    public effbdpattern_PatternCatalog getEffbdpattern_patterncatalog() {
        return effbdpattern_patterncatalog;
    }

    public void setEffbdpattern_patterncatalog(effbdpattern_PatternCatalog effbdpattern_patterncatalog) {
        this.effbdpattern_patterncatalog = effbdpattern_patterncatalog;
    }
    public List<effbdpattern_Condition> getEffbdpattern_conditions() {
        return effbdpattern_conditions;
    }

    public void addEffbdpattern_condition(Effbdpattern_condition effbdpattern_condition) {
        this.effbdpattern_conditions.add(effbdpattern_condition);
    }
    public List<effbdpattern_Domain> getEffbdpattern_domains() {
        return effbdpattern_domains;
    }

    public void addEffbdpattern_domain(Effbdpattern_domain effbdpattern_domain) {
        this.effbdpattern_domains.add(effbdpattern_domain);
    }
    public List<effbdpattern_Allocation> getEffbdpattern_allocations() {
        return effbdpattern_allocations;
    }

    public void addEffbdpattern_allocation(Effbdpattern_allocation effbdpattern_allocation) {
        this.effbdpattern_allocations.add(effbdpattern_allocation);
    }
    public List<effbdpattern_Feature> getEffbdpattern_features() {
        return effbdpattern_features;
    }

    public void addEffbdpattern_feature(Effbdpattern_feature effbdpattern_feature) {
        this.effbdpattern_features.add(effbdpattern_feature);
    }
    public List<effbdpattern_Problem> getEffbdpattern_problems() {
        return effbdpattern_problems;
    }

    public void addEffbdpattern_problem(Effbdpattern_problem effbdpattern_problem) {
        this.effbdpattern_problems.add(effbdpattern_problem);
    }
    public List<effbdpattern_FunctionProperty> getEffbdpattern_functionpropertys() {
        return effbdpattern_functionpropertys;
    }

    public void addEffbdpattern_functionproperty(Effbdpattern_functionproperty effbdpattern_functionproperty) {
        this.effbdpattern_functionpropertys.add(effbdpattern_functionproperty);
    }
    public List<effbdpattern_Model> getEffbdpattern_models() {
        return effbdpattern_models;
    }

    public void addEffbdpattern_model(Effbdpattern_model effbdpattern_model) {
        this.effbdpattern_models.add(effbdpattern_model);
    }

}