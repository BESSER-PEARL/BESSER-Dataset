





import java.util.List;
import java.util.ArrayList;

public class ale_Operation  {

    private String name;





    private ale_BehavioredClass ale_behavioredclass;


    public ale_Operation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ale_BehavioredClass getAle_behavioredclass() {
        return ale_behavioredclass;
    }

    public void setAle_behavioredclass(ale_BehavioredClass ale_behavioredclass) {
        this.ale_behavioredclass = ale_behavioredclass;
    }

}