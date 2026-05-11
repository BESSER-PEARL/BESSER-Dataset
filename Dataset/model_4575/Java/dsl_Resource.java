





import java.util.List;
import java.util.ArrayList;

public class dsl_Resource  {

    private String name;





    private List<dsl_State> dsl_states;




    private dsl_EnvironmentMetaData dsl_environmentmetadata;


    public dsl_Resource(
        String name    ) {
        this.name = name;
        this.dsl_states = new ArrayList<>();
    }

    public dsl_Resource(
        String name        ArrayList<dsl_State> dsl_states    ) {
        this.name = name;
        this.dsl_states = dsl_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<dsl_State> getDsl_states() {
        return dsl_states;
    }

    public void addDsl_state(Dsl_state dsl_state) {
        this.dsl_states.add(dsl_state);
    }
    public dsl_EnvironmentMetaData getDsl_environmentmetadata() {
        return dsl_environmentmetadata;
    }

    public void setDsl_environmentmetadata(dsl_EnvironmentMetaData dsl_environmentmetadata) {
        this.dsl_environmentmetadata = dsl_environmentmetadata;
    }

}