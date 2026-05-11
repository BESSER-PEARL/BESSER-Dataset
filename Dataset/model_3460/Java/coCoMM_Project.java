




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class coCoMM_Project  {

    private LocalDate date;
    private boolean target;
    private String name;





    private List<coCoMM_DecisionRule> cocomm_decisionrules;


    public coCoMM_Project(
        LocalDate date,        boolean target,        String name    ) {
        this.date = date;
        this.target = target;
        this.name = name;
        this.cocomm_decisionrules = new ArrayList<>();
    }

    public coCoMM_Project(
        LocalDate date,        boolean target,        String name        ArrayList<coCoMM_DecisionRule> cocomm_decisionrules    ) {
        this.date = date;
        this.target = target;
        this.name = name;
        this.cocomm_decisionrules = cocomm_decisionrules;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public boolean getTarget() {
        return target;
    }

    public void setTarget(boolean target) {
        this.target = target;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<coCoMM_DecisionRule> getCocomm_decisionrules() {
        return cocomm_decisionrules;
    }

    public void addCocomm_decisionrule(Cocomm_decisionrule cocomm_decisionrule) {
        this.cocomm_decisionrules.add(cocomm_decisionrule);
    }

}