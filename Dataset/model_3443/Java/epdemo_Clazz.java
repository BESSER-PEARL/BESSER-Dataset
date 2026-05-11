





import java.util.List;
import java.util.ArrayList;

public class epdemo_Clazz  {

    private String Name;
    private String Id;





    private epdemo_School epdemo_school;


    public epdemo_Clazz(
        String Name,        String Id    ) {
        this.Name = Name;
        this.Id = Id;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }

    public epdemo_School getEpdemo_school() {
        return epdemo_school;
    }

    public void setEpdemo_school(epdemo_School epdemo_school) {
        this.epdemo_school = epdemo_school;
    }

}