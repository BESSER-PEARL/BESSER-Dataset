





import java.util.List;
import java.util.ArrayList;

public class dsl_Ignorables  {

    private String AVOID_OBJECTS;





    private dsl_Task dsl_task;


    public dsl_Ignorables(
        String AVOID_OBJECTS    ) {
        this.AVOID_OBJECTS = AVOID_OBJECTS;
    }


    public String getAvoid_objects() {
        return AVOID_OBJECTS;
    }

    public void setAvoid_objects(String AVOID_OBJECTS) {
        this.AVOID_OBJECTS = AVOID_OBJECTS;
    }

    public dsl_Task getDsl_task() {
        return dsl_task;
    }

    public void setDsl_task(dsl_Task dsl_task) {
        this.dsl_task = dsl_task;
    }

}