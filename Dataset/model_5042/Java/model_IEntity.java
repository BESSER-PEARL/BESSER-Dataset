




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_IEntity  {

    private String id;
    private String modifiedBy;
    private String name;
    private LocalDate validFrom;
    private LocalDate validTo;
    private LocalDate dateAdded;
    private LocalDate modified;
    private String deleted;



    public model_IEntity(
        String id,        String modifiedBy,        String name,        LocalDate validFrom,        LocalDate validTo,        LocalDate dateAdded,        LocalDate modified,        String deleted    ) {
        this.id = id;
        this.modifiedBy = modifiedBy;
        this.name = name;
        this.validFrom = validFrom;
        this.validTo = validTo;
        this.dateAdded = dateAdded;
        this.modified = modified;
        this.deleted = deleted;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getModifiedby() {
        return modifiedBy;
    }

    public void setModifiedby(String modifiedBy) {
        this.modifiedBy = modifiedBy;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getValidfrom() {
        return validFrom;
    }

    public void setValidfrom(LocalDate validFrom) {
        this.validFrom = validFrom;
    }
    public LocalDate getValidto() {
        return validTo;
    }

    public void setValidto(LocalDate validTo) {
        this.validTo = validTo;
    }
    public LocalDate getDateadded() {
        return dateAdded;
    }

    public void setDateadded(LocalDate dateAdded) {
        this.dateAdded = dateAdded;
    }
    public LocalDate getModified() {
        return modified;
    }

    public void setModified(LocalDate modified) {
        this.modified = modified;
    }
    public String getDeleted() {
        return deleted;
    }

    public void setDeleted(String deleted) {
        this.deleted = deleted;
    }


}