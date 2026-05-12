





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_User_Permissions  {

    private int id;
    private int module;
    private String permissions;





    private Class_Diagram_for_Propsed_System_User_groups class_diagram_for_propsed_system_user_groups;


    public Class_Diagram_for_Propsed_System_User_Permissions(
        int id,        int module,        String permissions    ) {
        this.id = id;
        this.module = module;
        this.permissions = permissions;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getModule() {
        return module;
    }

    public void setModule(int module) {
        this.module = module;
    }
    public String getPermissions() {
        return permissions;
    }

    public void setPermissions(String permissions) {
        this.permissions = permissions;
    }

    public Class_Diagram_for_Propsed_System_User_groups getClass_diagram_for_propsed_system_user_groups() {
        return class_diagram_for_propsed_system_user_groups;
    }

    public void setClass_diagram_for_propsed_system_user_groups(Class_Diagram_for_Propsed_System_User_groups class_diagram_for_propsed_system_user_groups) {
        this.class_diagram_for_propsed_system_user_groups = class_diagram_for_propsed_system_user_groups;
    }

}