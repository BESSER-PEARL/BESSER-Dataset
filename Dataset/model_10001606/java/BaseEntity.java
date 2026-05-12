





import java.util.List;
import java.util.ArrayList;

public class BaseEntity  {

    private String Id;
    private String UpdatedDate;
    private String CreatedBy;
    private String CreatedDate;
    private boolean Active;
    private String UpdatedBy;



    public BaseEntity(
        String Id,        String UpdatedDate,        String CreatedBy,        String CreatedDate,        boolean Active,        String UpdatedBy    ) {
        this.Id = Id;
        this.UpdatedDate = UpdatedDate;
        this.CreatedBy = CreatedBy;
        this.CreatedDate = CreatedDate;
        this.Active = Active;
        this.UpdatedBy = UpdatedBy;
    }


    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getUpdateddate() {
        return UpdatedDate;
    }

    public void setUpdateddate(String UpdatedDate) {
        this.UpdatedDate = UpdatedDate;
    }
    public String getCreatedby() {
        return CreatedBy;
    }

    public void setCreatedby(String CreatedBy) {
        this.CreatedBy = CreatedBy;
    }
    public String getCreateddate() {
        return CreatedDate;
    }

    public void setCreateddate(String CreatedDate) {
        this.CreatedDate = CreatedDate;
    }
    public boolean getActive() {
        return Active;
    }

    public void setActive(boolean Active) {
        this.Active = Active;
    }
    public String getUpdatedby() {
        return UpdatedBy;
    }

    public void setUpdatedby(String UpdatedBy) {
        this.UpdatedBy = UpdatedBy;
    }


}