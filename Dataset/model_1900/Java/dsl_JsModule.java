





import java.util.List;
import java.util.ArrayList;

public class dsl_JsModule extends AbstractFrontElement {

    private String name;





    private dsl_ServiceFront dsl_servicefront;




    private dsl_Directory dsl_directory;


    public dsl_JsModule(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_ServiceFront getDsl_servicefront() {
        return dsl_servicefront;
    }

    public void setDsl_servicefront(dsl_ServiceFront dsl_servicefront) {
        this.dsl_servicefront = dsl_servicefront;
    }
    public dsl_Directory getDsl_directory() {
        return dsl_directory;
    }

    public void setDsl_directory(dsl_Directory dsl_directory) {
        this.dsl_directory = dsl_directory;
    }

}