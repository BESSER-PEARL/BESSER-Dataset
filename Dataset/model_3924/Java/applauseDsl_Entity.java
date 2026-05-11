





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_Entity extends Type {






    private applauseDsl_Entity applausedsl_entity;




    private List<applauseDsl_Property> applausedsl_propertys;


    public applauseDsl_Entity(
    ) {
        super(
        );
        this.applausedsl_propertys = new ArrayList<>();
    }

    public applauseDsl_Entity(
        ArrayList<applauseDsl_Property> applausedsl_propertys    ) {
        this.applausedsl_propertys = applausedsl_propertys;
    }


    public applauseDsl_Entity getApplausedsl_entity() {
        return applausedsl_entity;
    }

    public void setApplausedsl_entity(applauseDsl_Entity applausedsl_entity) {
        this.applausedsl_entity = applausedsl_entity;
    }
    public List<applauseDsl_Property> getApplausedsl_propertys() {
        return applausedsl_propertys;
    }

    public void addApplausedsl_property(Applausedsl_property applausedsl_property) {
        this.applausedsl_propertys.add(applausedsl_property);
    }

}