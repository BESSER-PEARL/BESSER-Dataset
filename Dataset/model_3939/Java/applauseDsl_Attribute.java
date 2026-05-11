





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_Attribute  {

    private String name;
    private boolean many;





    private applauseDsl_Entity applausedsl_entity;




    private applauseDsl_Type applausedsl_type;




    private applauseDsl_EntityMemberCallTail applausedsl_entitymembercalltail;




    private applauseDsl_EntityMemberCall applausedsl_entitymembercall;




    private applauseDsl_AttributeReference applausedsl_attributereference;


    public applauseDsl_Attribute(
        String name,        boolean many    ) {
        this.name = name;
        this.many = many;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public applauseDsl_Entity getApplausedsl_entity() {
        return applausedsl_entity;
    }

    public void setApplausedsl_entity(applauseDsl_Entity applausedsl_entity) {
        this.applausedsl_entity = applausedsl_entity;
    }
    public applauseDsl_Type getApplausedsl_type() {
        return applausedsl_type;
    }

    public void setApplausedsl_type(applauseDsl_Type applausedsl_type) {
        this.applausedsl_type = applausedsl_type;
    }
    public applauseDsl_EntityMemberCallTail getApplausedsl_entitymembercalltail() {
        return applausedsl_entitymembercalltail;
    }

    public void setApplausedsl_entitymembercalltail(applauseDsl_EntityMemberCallTail applausedsl_entitymembercalltail) {
        this.applausedsl_entitymembercalltail = applausedsl_entitymembercalltail;
    }
    public applauseDsl_EntityMemberCall getApplausedsl_entitymembercall() {
        return applausedsl_entitymembercall;
    }

    public void setApplausedsl_entitymembercall(applauseDsl_EntityMemberCall applausedsl_entitymembercall) {
        this.applausedsl_entitymembercall = applausedsl_entitymembercall;
    }
    public applauseDsl_AttributeReference getApplausedsl_attributereference() {
        return applausedsl_attributereference;
    }

    public void setApplausedsl_attributereference(applauseDsl_AttributeReference applausedsl_attributereference) {
        this.applausedsl_attributereference = applausedsl_attributereference;
    }

}