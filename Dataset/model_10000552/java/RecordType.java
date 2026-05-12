





import java.util.List;
import java.util.ArrayList;

public class RecordType  {

    private String crm_id;
    private String updated_by;
    private String id;
    private String description;
    private String name;
    private String deleted;



    public RecordType(
        String crm_id,        String updated_by,        String id,        String description,        String name,        String deleted    ) {
        this.crm_id = crm_id;
        this.updated_by = updated_by;
        this.id = id;
        this.description = description;
        this.name = name;
        this.deleted = deleted;
    }


    public String getCrm_id() {
        return crm_id;
    }

    public void setCrm_id(String crm_id) {
        this.crm_id = crm_id;
    }
    public String getUpdated_by() {
        return updated_by;
    }

    public void setUpdated_by(String updated_by) {
        this.updated_by = updated_by;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDeleted() {
        return deleted;
    }

    public void setDeleted(String deleted) {
        this.deleted = deleted;
    }


}