





import java.util.List;
import java.util.ArrayList;

public class unql_Connection  {

    private String name;
    private String username;
    private String url;
    private String password;





    private unql_Program unql_program;


    public unql_Connection(
        String name,        String username,        String url,        String password    ) {
        this.name = name;
        this.username = username;
        this.url = url;
        this.password = password;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public unql_Program getUnql_program() {
        return unql_program;
    }

    public void setUnql_program(unql_Program unql_program) {
        this.unql_program = unql_program;
    }

}