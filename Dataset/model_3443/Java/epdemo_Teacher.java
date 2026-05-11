





import java.util.List;
import java.util.ArrayList;

public class epdemo_Teacher  {

    private String Id;
    private String Name;





    private epdemo_School epdemo_school;




    private epdemo_Clazz epdemo_clazz;


    public epdemo_Teacher(
        String Id,        String Name    ) {
        this.Id = Id;
        this.Name = Name;
    }


    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public epdemo_School getEpdemo_school() {
        return epdemo_school;
    }

    public void setEpdemo_school(epdemo_School epdemo_school) {
        this.epdemo_school = epdemo_school;
    }
    public epdemo_Clazz getEpdemo_clazz() {
        return epdemo_clazz;
    }

    public void setEpdemo_clazz(epdemo_Clazz epdemo_clazz) {
        this.epdemo_clazz = epdemo_clazz;
    }

}