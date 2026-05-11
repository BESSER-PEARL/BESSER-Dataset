





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_Function extends ModelElement, SequenceNode {

    private String domain;





    private effbdpattern_PatternModel effbdpattern_patternmodel;




    private effbdpattern_Allocation effbdpattern_allocation;




    private effbdpattern_Function effbdpattern_function;




    private effbdpattern_Model effbdpattern_model;




    private effbdpattern_Function effbdpattern_function;


    public effbdpattern_Function(
        String domain    ) {
        super(
        );
        this.domain = domain;
    }


    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public effbdpattern_PatternModel getEffbdpattern_patternmodel() {
        return effbdpattern_patternmodel;
    }

    public void setEffbdpattern_patternmodel(effbdpattern_PatternModel effbdpattern_patternmodel) {
        this.effbdpattern_patternmodel = effbdpattern_patternmodel;
    }
    public effbdpattern_Allocation getEffbdpattern_allocation() {
        return effbdpattern_allocation;
    }

    public void setEffbdpattern_allocation(effbdpattern_Allocation effbdpattern_allocation) {
        this.effbdpattern_allocation = effbdpattern_allocation;
    }
    public effbdpattern_Function getEffbdpattern_function() {
        return effbdpattern_function;
    }

    public void setEffbdpattern_function(effbdpattern_Function effbdpattern_function) {
        this.effbdpattern_function = effbdpattern_function;
    }
    public effbdpattern_Model getEffbdpattern_model() {
        return effbdpattern_model;
    }

    public void setEffbdpattern_model(effbdpattern_Model effbdpattern_model) {
        this.effbdpattern_model = effbdpattern_model;
    }
    public effbdpattern_Function getEffbdpattern_function() {
        return effbdpattern_function;
    }

    public void setEffbdpattern_function(effbdpattern_Function effbdpattern_function) {
        this.effbdpattern_function = effbdpattern_function;
    }

}