





import java.util.List;
import java.util.ArrayList;

public class basicFsmEnv_VarDecl  {

    private String value;
    private String name;





    private basicFsmEnv_State basicfsmenv_state;


    public basicFsmEnv_VarDecl(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public basicFsmEnv_State getBasicfsmenv_state() {
        return basicfsmenv_state;
    }

    public void setBasicfsmenv_state(basicFsmEnv_State basicfsmenv_state) {
        this.basicfsmenv_state = basicfsmenv_state;
    }

}