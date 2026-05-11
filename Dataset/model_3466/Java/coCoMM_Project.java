




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class coCoMM_Project  {

    private LocalDate date;
    private String name;
    private boolean target;





    private coCoMM_CoCo cocomm_coco;




    private List<coCoMM_SolutionConstraint> cocomm_solutionconstraints;


    public coCoMM_Project(
        LocalDate date,        String name,        boolean target    ) {
        this.date = date;
        this.name = name;
        this.target = target;
        this.cocomm_solutionconstraints = new ArrayList<>();
    }

    public coCoMM_Project(
        LocalDate date,        String name,        boolean target        ArrayList<coCoMM_SolutionConstraint> cocomm_solutionconstraints    ) {
        this.date = date;
        this.name = name;
        this.target = target;
        this.cocomm_solutionconstraints = cocomm_solutionconstraints;
    }

    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public List<coCoMM_SolutionConstraint> getCocomm_solutionconstraints() {
        return cocomm_solutionconstraints;
    }

    public void addCocomm_solutionconstraint(Cocomm_solutionconstraint cocomm_solutionconstraint) {
        this.cocomm_solutionconstraints.add(cocomm_solutionconstraint);
    }

}