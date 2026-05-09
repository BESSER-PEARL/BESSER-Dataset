





import java.util.List;
import java.util.ArrayList;

public class dsl_SpecialEntity  {






    private dsl_EntityName dsl_entityname;




    private List<dsl_Property> dsl_propertys;


    public dsl_SpecialEntity(
    ) {
        this.dsl_propertys = new ArrayList<>();
    }

    public dsl_SpecialEntity(
        ArrayList<dsl_Property> dsl_propertys    ) {
        this.dsl_propertys = dsl_propertys;
    }


    public dsl_EntityName getDsl_entityname() {
        return dsl_entityname;
    }

    public void setDsl_entityname(dsl_EntityName dsl_entityname) {
        this.dsl_entityname = dsl_entityname;
    }
    public List<dsl_Property> getDsl_propertys() {
        return dsl_propertys;
    }

    public void addDsl_property(Dsl_property dsl_property) {
        this.dsl_propertys.add(dsl_property);
    }

}