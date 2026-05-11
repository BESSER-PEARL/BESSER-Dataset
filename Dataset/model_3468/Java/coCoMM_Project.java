




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class coCoMM_Project  {

    private String name;
    private LocalDate date;
    private boolean target;





    private coCoMM_CoCo cocomm_coco;




    private List<coCoMM_ConfigurationConstraint> cocomm_configurationconstraints;




    private List<coCoMM_SolutionConstraint> cocomm_solutionconstraints;


    public coCoMM_Project(
        String name,        LocalDate date,        boolean target    ) {
        this.name = name;
        this.date = date;
        this.target = target;
        this.cocomm_configurationconstraints = new ArrayList<>();
        this.cocomm_solutionconstraints = new ArrayList<>();
    }

    public coCoMM_Project(
        String name,        LocalDate date,        boolean target        ArrayList<coCoMM_ConfigurationConstraint> cocomm_configurationconstraints,        ArrayList<coCoMM_SolutionConstraint> cocomm_solutionconstraints    ) {
        this.name = name;
        this.date = date;
        this.target = target;
        this.cocomm_configurationconstraints = cocomm_configurationconstraints;
        this.cocomm_solutionconstraints = cocomm_solutionconstraints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public coCoMM_CoCo getCocomm_coco() {
        return cocomm_coco;
    }

    public void setCocomm_coco(coCoMM_CoCo cocomm_coco) {
        this.cocomm_coco = cocomm_coco;
    }
    public List<coCoMM_ConfigurationConstraint> getCocomm_configurationconstraints() {
        return cocomm_configurationconstraints;
    }

    public void addCocomm_configurationconstraint(Cocomm_configurationconstraint cocomm_configurationconstraint) {
        this.cocomm_configurationconstraints.add(cocomm_configurationconstraint);
    }
    public List<coCoMM_SolutionConstraint> getCocomm_solutionconstraints() {
        return cocomm_solutionconstraints;
    }

    public void addCocomm_solutionconstraint(Cocomm_solutionconstraint cocomm_solutionconstraint) {
        this.cocomm_solutionconstraints.add(cocomm_solutionconstraint);
    }

}