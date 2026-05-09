




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_R4EItem extends R4EIDComponent, Item {

    private LocalDate submitted;
    private String addedById;
    private String authorRep;
    private String description;
    private String ProjectURIs;
    private String repositoryRef;





    private model_R4EUser model_r4euser;


    public model_R4EItem(
        LocalDate submitted,        String addedById,        String authorRep,        String description,        String ProjectURIs,        String repositoryRef    ) {
        super(
        );
        this.submitted = submitted;
        this.addedById = addedById;
        this.authorRep = authorRep;
        this.description = description;
        this.ProjectURIs = ProjectURIs;
        this.repositoryRef = repositoryRef;
    }


    public LocalDate getSubmitted() {
        return submitted;
    }

    public void setSubmitted(LocalDate submitted) {
        this.submitted = submitted;
    }
    public String getAddedbyid() {
        return addedById;
    }

    public void setAddedbyid(String addedById) {
        this.addedById = addedById;
    }
    public String getAuthorrep() {
        return authorRep;
    }

    public void setAuthorrep(String authorRep) {
        this.authorRep = authorRep;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getProjecturis() {
        return ProjectURIs;
    }

    public void setProjecturis(String ProjectURIs) {
        this.ProjectURIs = ProjectURIs;
    }
    public String getRepositoryref() {
        return repositoryRef;
    }

    public void setRepositoryref(String repositoryRef) {
        this.repositoryRef = repositoryRef;
    }

    public model_R4EUser getModel_r4euser() {
        return model_r4euser;
    }

    public void setModel_r4euser(model_R4EUser model_r4euser) {
        this.model_r4euser = model_r4euser;
    }

}