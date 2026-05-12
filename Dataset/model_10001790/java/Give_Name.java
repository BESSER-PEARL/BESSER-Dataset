





import java.util.List;
import java.util.ArrayList;

public class Give_Name  {

    private String Name;





    private Update_Data update_data;


    public Give_Name(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Update_Data getUpdate_data() {
        return update_data;
    }

    public void setUpdate_data(Update_Data update_data) {
        this.update_data = update_data;
    }

}