




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class coCoMM_Project  {

    private boolean target;
    private String name;
    private LocalDate date;





    private coCoMM_CoCo cocomm_coco;




    private List<coCoMM_SolutionConstraint> cocomm_solutionconstraints;


    public coCoMM_Project(
        boolean target,        String name,        LocalDate date    ) {
        this.target = target;
        this.name = name;
        this.date = date;
        this.cocomm_solutionconstraints = new ArrayList<>();
    }

    public coCoMM_Project(
        boolean target,        String name,        LocalDate date        ArrayList<coCoMM_SolutionConstraint> cocomm_solutionconstraints    ) {
        this.target = target;
        this.name = name;
        this.date = date;
        this.cocomm_solutionconstraints = cocomm_solutionconstraints;
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
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public coCoMM_CoCo getCocomm_coco() {
        return cocomm_coco;
    }

    public void setCocomm_coco(coCoMM_CoCo cocomm_coco) {
        this.cocomm_coco = cocomm_coco;
    }
    public List<coCoMM_SolutionConstraint> getCocomm_solutionconstraints() {
        return cocomm_solutionconstraints;
    }

    public void addCocomm_solutionconstraint(Cocomm_solutionconstraint cocomm_solutionconstraint) {
        this.cocomm_solutionconstraints.add(cocomm_solutionconstraint);
    }

}