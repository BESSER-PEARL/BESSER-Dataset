




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class itm_Issue  {

    private String name;
    private float estimatedHours;
    private String description;
    private String priority;
    private LocalDate completedDate;
    private LocalDate dueDate;
    private float elapsedHours;
    private String status;
    private float doneRatio;





    private itm_IssueCategory itm_issuecategory;




    private itm_Version itm_version;




    private itm_Member itm_member;




    private itm_IssueDependency itm_issuedependency;




    private List<itm_IssueDependency> itm_issuedependencys;




    private itm_Tracker itm_tracker;




    private itm_Member itm_member;


    public itm_Issue(
        String name,        float estimatedHours,        String description,        String priority,        LocalDate completedDate,        LocalDate dueDate,        float elapsedHours,        String status,        float doneRatio    ) {
        this.name = name;
        this.estimatedHours = estimatedHours;
        this.description = description;
        this.priority = priority;
        this.completedDate = completedDate;
        this.dueDate = dueDate;
        this.elapsedHours = elapsedHours;
        this.status = status;
        this.doneRatio = doneRatio;
        this.itm_issuedependencys = new ArrayList<>();
    }

    public itm_Issue(
        String name,        float estimatedHours,        String description,        String priority,        LocalDate completedDate,        LocalDate dueDate,        float elapsedHours,        String status,        float doneRatio        ArrayList<itm_IssueDependency> itm_issuedependencys    ) {
        this.name = name;
        this.estimatedHours = estimatedHours;
        this.description = description;
        this.priority = priority;
        this.completedDate = completedDate;
        this.dueDate = dueDate;
        this.elapsedHours = elapsedHours;
        this.status = status;
        this.doneRatio = doneRatio;
        this.itm_issuedependencys = itm_issuedependencys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getEstimatedhours() {
        return estimatedHours;
    }

    public void setEstimatedhours(float estimatedHours) {
        this.estimatedHours = estimatedHours;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public LocalDate getCompleteddate() {
        return completedDate;
    }

    public void setCompleteddate(LocalDate completedDate) {
        this.completedDate = completedDate;
    }
    public LocalDate getDuedate() {
        return dueDate;
    }

    public void setDuedate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }
    public float getElapsedhours() {
        return elapsedHours;
    }

    public void setElapsedhours(float elapsedHours) {
        this.elapsedHours = elapsedHours;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public float getDoneratio() {
        return doneRatio;
    }

    public void setDoneratio(float doneRatio) {
        this.doneRatio = doneRatio;
    }

    public itm_IssueCategory getItm_issuecategory() {
        return itm_issuecategory;
    }

    public void setItm_issuecategory(itm_IssueCategory itm_issuecategory) {
        this.itm_issuecategory = itm_issuecategory;
    }
    public itm_Version getItm_version() {
        return itm_version;
    }

    public void setItm_version(itm_Version itm_version) {
        this.itm_version = itm_version;
    }
    public itm_Member getItm_member() {
        return itm_member;
    }

    public void setItm_member(itm_Member itm_member) {
        this.itm_member = itm_member;
    }
    public itm_IssueDependency getItm_issuedependency() {
        return itm_issuedependency;
    }

    public void setItm_issuedependency(itm_IssueDependency itm_issuedependency) {
        this.itm_issuedependency = itm_issuedependency;
    }
    public List<itm_IssueDependency> getItm_issuedependencys() {
        return itm_issuedependencys;
    }

    public void addItm_issuedependency(Itm_issuedependency itm_issuedependency) {
        this.itm_issuedependencys.add(itm_issuedependency);
    }
    public itm_Tracker getItm_tracker() {
        return itm_tracker;
    }

    public void setItm_tracker(itm_Tracker itm_tracker) {
        this.itm_tracker = itm_tracker;
    }
    public itm_Member getItm_member() {
        return itm_member;
    }

    public void setItm_member(itm_Member itm_member) {
        this.itm_member = itm_member;
    }

}