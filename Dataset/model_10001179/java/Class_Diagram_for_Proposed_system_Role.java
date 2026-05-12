





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_Role  {

    private String roleName;
    private String id;
    private String description;





    private Class_Diagram_for_Proposed_system_User class_diagram_for_proposed_system_user;


    public Class_Diagram_for_Proposed_system_Role(
        String roleName,        String id,        String description    ) {
        this.roleName = roleName;
        this.id = id;
        this.description = description;
    }


    public String getRolename() {
        return roleName;
    }

    public void setRolename(String roleName) {
        this.roleName = roleName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Class_Diagram_for_Proposed_system_User getClass_diagram_for_proposed_system_user() {
        return class_diagram_for_proposed_system_user;
    }

    public void setClass_diagram_for_proposed_system_user(Class_Diagram_for_Proposed_system_User class_diagram_for_proposed_system_user) {
        this.class_diagram_for_proposed_system_user = class_diagram_for_proposed_system_user;
    }

}