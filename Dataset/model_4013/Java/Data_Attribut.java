





import java.util.List;
import java.util.ArrayList;

public class Data_Attribut  {

    private String Name;
    private boolean Static;
    private String Visibility;
    private String Type;





    private Data_Class data_class;


    public Data_Attribut(
        String Name,        boolean Static,        String Visibility,        String Type    ) {
        this.Name = Name;
        this.Static = Static;
        this.Visibility = Visibility;
        this.Type = Type;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public boolean getStatic() {
        return Static;
    }

    public void setStatic(boolean Static) {
        this.Static = Static;
    }
    public String getVisibility() {
        return Visibility;
    }

    public void setVisibility(String Visibility) {
        this.Visibility = Visibility;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public Data_Class getData_class() {
        return data_class;
    }

    public void setData_class(Data_Class data_class) {
        this.data_class = data_class;
    }

}