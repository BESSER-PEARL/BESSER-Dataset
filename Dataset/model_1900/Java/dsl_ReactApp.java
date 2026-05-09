





import java.util.List;
import java.util.ArrayList;

public class dsl_ReactApp extends AbstractFrontElement {






    private dsl_Directory dsl_directory;




    private dsl_Technology dsl_technology;




    private dsl_JsModule dsl_jsmodule;


    public dsl_ReactApp(
    ) {
        super(
        );
    }



    public dsl_Directory getDsl_directory() {
        return dsl_directory;
    }

    public void setDsl_directory(dsl_Directory dsl_directory) {
        this.dsl_directory = dsl_directory;
    }
    public dsl_Technology getDsl_technology() {
        return dsl_technology;
    }

    public void setDsl_technology(dsl_Technology dsl_technology) {
        this.dsl_technology = dsl_technology;
    }
    public dsl_JsModule getDsl_jsmodule() {
        return dsl_jsmodule;
    }

    public void setDsl_jsmodule(dsl_JsModule dsl_jsmodule) {
        this.dsl_jsmodule = dsl_jsmodule;
    }

}