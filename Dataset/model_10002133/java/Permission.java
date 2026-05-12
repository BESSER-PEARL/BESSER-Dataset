





import java.util.List;
import java.util.ArrayList;

public class Permission  {

    private None Crud;
    private None Allow;
    private int Id;
    private String Name;
    private None Scope;



    public Permission(
        None Crud,        None Allow,        int Id,        String Name,        None Scope    ) {
        this.Crud = Crud;
        this.Allow = Allow;
        this.Id = Id;
        this.Name = Name;
        this.Scope = Scope;
    }


    public None getCrud() {
        return Crud;
    }

    public void setCrud(None Crud) {
        this.Crud = Crud;
    }
    public None getAllow() {
        return Allow;
    }

    public void setAllow(None Allow) {
        this.Allow = Allow;
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
    public None getScope() {
        return Scope;
    }

    public void setScope(None Scope) {
        this.Scope = Scope;
    }


}