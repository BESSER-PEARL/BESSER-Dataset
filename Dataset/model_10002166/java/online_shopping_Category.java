





import java.util.List;
import java.util.ArrayList;

public class online_shopping_Category  {

    private None Catemegory_Name;
    private String Category_ID;
    private None Description;
    private String Department_ID;





    private online_shopping_Deoartment online_shopping_deoartment;


    public online_shopping_Category(
        None Catemegory_Name,        String Category_ID,        None Description,        String Department_ID    ) {
        this.Catemegory_Name = Catemegory_Name;
        this.Category_ID = Category_ID;
        this.Description = Description;
        this.Department_ID = Department_ID;
    }


    public None getCatemegory_name() {
        return Catemegory_Name;
    }

    public void setCatemegory_name(None Catemegory_Name) {
        this.Catemegory_Name = Catemegory_Name;
    }
    public String getCategory_id() {
        return Category_ID;
    }

    public void setCategory_id(String Category_ID) {
        this.Category_ID = Category_ID;
    }
    public None getDescription() {
        return Description;
    }

    public void setDescription(None Description) {
        this.Description = Description;
    }
    public String getDepartment_id() {
        return Department_ID;
    }

    public void setDepartment_id(String Department_ID) {
        this.Department_ID = Department_ID;
    }

    public online_shopping_Deoartment getOnline_shopping_deoartment() {
        return online_shopping_deoartment;
    }

    public void setOnline_shopping_deoartment(online_shopping_Deoartment online_shopping_deoartment) {
        this.online_shopping_deoartment = online_shopping_deoartment;
    }

}