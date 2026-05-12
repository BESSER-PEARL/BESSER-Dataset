





import java.util.List;
import java.util.ArrayList;

public class Usuario_Interface  {






    private List<Role> roles;


    public Usuario_Interface(
    ) {
        this.roles = new ArrayList<>();
    }

    public Usuario_Interface(
        ArrayList<Role> roles    ) {
        this.roles = roles;
    }


    public List<Role> getRoles() {
        return roles;
    }

    public void addRole(Role role) {
        this.roles.add(role);
    }

}