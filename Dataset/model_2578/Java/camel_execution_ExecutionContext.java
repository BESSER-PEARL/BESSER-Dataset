




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class camel_execution_ExecutionContext  {

    private LocalDate startTime;
    private LocalDate endTime;
    private String name;
    private float totalCost;





    private MonetaryUnit monetaryunit;




    private DeploymentModel deploymentmodel;




    private RequirementGroup requirementgroup;


    public camel_execution_ExecutionContext(
        LocalDate startTime,        LocalDate endTime,        String name,        float totalCost    ) {
        this.startTime = startTime;
        this.endTime = endTime;
        this.name = name;
        this.totalCost = totalCost;
    }


    public LocalDate getStarttime() {
        return startTime;
    }

    public void setStarttime(LocalDate startTime) {
        this.startTime = startTime;
    }
    public LocalDate getEndtime() {
        return endTime;
    }

    public void setEndtime(LocalDate endTime) {
        this.endTime = endTime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getTotalcost() {
        return totalCost;
    }

    public void setTotalcost(float totalCost) {
        this.totalCost = totalCost;
    }

    public MonetaryUnit getMonetaryunit() {
        return monetaryunit;
    }

    public void setMonetaryunit(MonetaryUnit monetaryunit) {
        this.monetaryunit = monetaryunit;
    }
    public DeploymentModel getDeploymentmodel() {
        return deploymentmodel;
    }

    public void setDeploymentmodel(DeploymentModel deploymentmodel) {
        this.deploymentmodel = deploymentmodel;
    }
    public RequirementGroup getRequirementgroup() {
        return requirementgroup;
    }

    public void setRequirementgroup(RequirementGroup requirementgroup) {
        this.requirementgroup = requirementgroup;
    }

}