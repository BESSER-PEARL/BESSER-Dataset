





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private int ScopeId;
    private int Id;
    private String Name;
    private None Users;
    private None Permissions;
    private None Scope;



    public Group(
        int ScopeId,        int Id,        String Name,        None Users,        None Permissions,        None Scope    ) {
        this.ScopeId = ScopeId;
        this.Id = Id;
        this.Name = Name;
        this.Users = Users;
        this.Permissions = Permissions;
        this.Scope = Scope;
    }


    public int getScopeid() {
        return ScopeId;
    }

    public void setScopeid(int ScopeId) {
        this.ScopeId = ScopeId;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public None getUsers() {
        return Users;
    }

    public void setUsers(None Users) {
        this.Users = Users;
    }
    public None getPermissions() {
        return Permissions;
    }

    public void setPermissions(None Permissions) {
        this.Permissions = Permissions;
    }
    public None getScope() {
        return Scope;
    }

    public void setScope(None Scope) {
        this.Scope = Scope;
    }


}