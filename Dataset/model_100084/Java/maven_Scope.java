





import java.util.List;
import java.util.ArrayList;

public class maven_Scope  {

    private String name;
    private boolean exclude;





    private maven_Scopes maven_scopes;


    public maven_Scope(
        String name,        boolean exclude    ) {
        this.name = name;
        this.exclude = exclude;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getExclude() {
        return exclude;
    }

    public void setExclude(boolean exclude) {
        this.exclude = exclude;
    }

    public maven_Scopes getMaven_scopes() {
        return maven_scopes;
    }

    public void setMaven_scopes(maven_Scopes maven_scopes) {
        this.maven_scopes = maven_scopes;
    }

}