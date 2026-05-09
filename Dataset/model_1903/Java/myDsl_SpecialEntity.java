





import java.util.List;
import java.util.ArrayList;

public class myDsl_SpecialEntity  {






    private myDsl_EntityName mydsl_entityname;




    private List<myDsl_Property> mydsl_propertys;


    public myDsl_SpecialEntity(
    ) {
        this.mydsl_propertys = new ArrayList<>();
    }

    public myDsl_SpecialEntity(
        ArrayList<myDsl_Property> mydsl_propertys    ) {
        this.mydsl_propertys = mydsl_propertys;
    }


    public myDsl_EntityName getMydsl_entityname() {
        return mydsl_entityname;
    }

    public void setMydsl_entityname(myDsl_EntityName mydsl_entityname) {
        this.mydsl_entityname = mydsl_entityname;
    }
    public List<myDsl_Property> getMydsl_propertys() {
        return mydsl_propertys;
    }

    public void addMydsl_property(Mydsl_property mydsl_property) {
        this.mydsl_propertys.add(mydsl_property);
    }

}