




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class AbstractEntity  {

    private None modifiedBy;
    private None createdBy;
    private LocalDate modifiedAt;
    private String id;
    private None createdAt;



    public AbstractEntity(
        None modifiedBy,        None createdBy,        LocalDate modifiedAt,        String id,        None createdAt    ) {
        this.modifiedBy = modifiedBy;
        this.createdBy = createdBy;
        this.modifiedAt = modifiedAt;
        this.id = id;
        this.createdAt = createdAt;
    }


    public None getModifiedby() {
        return modifiedBy;
    }

    public void setModifiedby(None modifiedBy) {
        this.modifiedBy = modifiedBy;
    }
    public None getCreatedby() {
        return createdBy;
    }

    public void setCreatedby(None createdBy) {
        this.createdBy = createdBy;
    }
    public LocalDate getModifiedat() {
        return modifiedAt;
    }

    public void setModifiedat(LocalDate modifiedAt) {
        this.modifiedAt = modifiedAt;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public None getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(None createdAt) {
        this.createdAt = createdAt;
    }


}