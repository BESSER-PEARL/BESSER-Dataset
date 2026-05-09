





import java.util.List;
import java.util.ArrayList;

public class dsl_AbstractFrontElement  {






    private dsl_Container dsl_container;




    private dsl_Reducer dsl_reducer;




    private dsl_RouterComponent dsl_routercomponent;




    private dsl_ReactApp dsl_reactapp;




    private dsl_Visualizer dsl_visualizer;


    public dsl_AbstractFrontElement(
    ) {
    }



    public dsl_Container getDsl_container() {
        return dsl_container;
    }

    public void setDsl_container(dsl_Container dsl_container) {
        this.dsl_container = dsl_container;
    }
    public dsl_Reducer getDsl_reducer() {
        return dsl_reducer;
    }

    public void setDsl_reducer(dsl_Reducer dsl_reducer) {
        this.dsl_reducer = dsl_reducer;
    }
    public dsl_RouterComponent getDsl_routercomponent() {
        return dsl_routercomponent;
    }

    public void setDsl_routercomponent(dsl_RouterComponent dsl_routercomponent) {
        this.dsl_routercomponent = dsl_routercomponent;
    }
    public dsl_ReactApp getDsl_reactapp() {
        return dsl_reactapp;
    }

    public void setDsl_reactapp(dsl_ReactApp dsl_reactapp) {
        this.dsl_reactapp = dsl_reactapp;
    }
    public dsl_Visualizer getDsl_visualizer() {
        return dsl_visualizer;
    }

    public void setDsl_visualizer(dsl_Visualizer dsl_visualizer) {
        this.dsl_visualizer = dsl_visualizer;
    }

}