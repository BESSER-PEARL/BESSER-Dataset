





import java.util.List;
import java.util.ArrayList;

public class dsl_Functionality extends AbstractFrontElement {

    private String name;





    private dsl_ServiceFront dsl_servicefront;




    private dsl_Visualizer dsl_visualizer;




    private dsl_ReactApp dsl_reactapp;




    private dsl_Directory dsl_directory;




    private dsl_RouterComponent dsl_routercomponent;


    public dsl_Functionality(
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
    public dsl_Visualizer getDsl_visualizer() {
        return dsl_visualizer;
    }

    public void setDsl_visualizer(dsl_Visualizer dsl_visualizer) {
        this.dsl_visualizer = dsl_visualizer;
    }
    public dsl_ReactApp getDsl_reactapp() {
        return dsl_reactapp;
    }

    public void setDsl_reactapp(dsl_ReactApp dsl_reactapp) {
        this.dsl_reactapp = dsl_reactapp;
    }
    public dsl_Directory getDsl_directory() {
        return dsl_directory;
    }

    public void setDsl_directory(dsl_Directory dsl_directory) {
        this.dsl_directory = dsl_directory;
    }
    public dsl_RouterComponent getDsl_routercomponent() {
        return dsl_routercomponent;
    }

    public void setDsl_routercomponent(dsl_RouterComponent dsl_routercomponent) {
        this.dsl_routercomponent = dsl_routercomponent;
    }

}