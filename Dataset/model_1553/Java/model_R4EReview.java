




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_R4EReview extends Review, R4EReviewComponent {

    private LocalDate modifiedDate;
    private String name;
    private String project;
    private String referenceMaterial;
    private String entryCriteria;
    private String extraNotes;
    private String type;
    private String objectives;
    private LocalDate startDate;
    private LocalDate endDate;
    private String components;
    private LocalDate dueDate;





    private model_R4EAnomaly model_r4eanomaly;


    public model_R4EReview(
        LocalDate modifiedDate,        String name,        String project,        String referenceMaterial,        String entryCriteria,        String extraNotes,        String type,        String objectives,        LocalDate startDate,        LocalDate endDate,        String components,        LocalDate dueDate    ) {
        super(
        );
        this.modifiedDate = modifiedDate;
        this.name = name;
        this.project = project;
        this.referenceMaterial = referenceMaterial;
        this.entryCriteria = entryCriteria;
        this.extraNotes = extraNotes;
        this.type = type;
        this.objectives = objectives;
        this.startDate = startDate;
        this.endDate = endDate;
        this.components = components;
        this.dueDate = dueDate;
    }


    public LocalDate getModifieddate() {
        return modifiedDate;
    }

    public void setModifieddate(LocalDate modifiedDate) {
        this.modifiedDate = modifiedDate;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getProject() {
        return project;
    }

    public void setProject(String project) {
        this.project = project;
    }
    public String getReferencematerial() {
        return referenceMaterial;
    }

    public void setReferencematerial(String referenceMaterial) {
        this.referenceMaterial = referenceMaterial;
    }
    public String getEntrycriteria() {
        return entryCriteria;
    }

    public void setEntrycriteria(String entryCriteria) {
        this.entryCriteria = entryCriteria;
    }
    public String getExtranotes() {
        return extraNotes;
    }

    public void setExtranotes(String extraNotes) {
        this.extraNotes = extraNotes;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getObjectives() {
        return objectives;
    }

    public void setObjectives(String objectives) {
        this.objectives = objectives;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public String getComponents() {
        return components;
    }

    public void setComponents(String components) {
        this.components = components;
    }
    public LocalDate getDuedate() {
        return dueDate;
    }

    public void setDuedate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }

    public model_R4EAnomaly getModel_r4eanomaly() {
        return model_r4eanomaly;
    }

    public void setModel_r4eanomaly(model_R4EAnomaly model_r4eanomaly) {
        this.model_r4eanomaly = model_r4eanomaly;
    }

}