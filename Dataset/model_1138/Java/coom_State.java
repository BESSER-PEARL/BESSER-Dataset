





import java.util.List;
import java.util.ArrayList;

public class coom_State  {

    private String name;
    private boolean initial;





    private coom_ComponentOnOffManifest coom_componentonoffmanifest;


    public coom_State(
        String name,        boolean initial    ) {
        this.name = name;
        this.initial = initial;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public coom_ComponentOnOffManifest getCoom_componentonoffmanifest() {
        return coom_componentonoffmanifest;
    }

    public void setCoom_componentonoffmanifest(coom_ComponentOnOffManifest coom_componentonoffmanifest) {
        this.coom_componentonoffmanifest = coom_componentonoffmanifest;
    }

}