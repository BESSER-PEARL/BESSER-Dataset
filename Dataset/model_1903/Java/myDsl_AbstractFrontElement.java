





import java.util.List;
import java.util.ArrayList;

public class myDsl_AbstractFrontElement  {






    private myDsl_ReactApp mydsl_reactapp;




    private myDsl_Reducer mydsl_reducer;




    private myDsl_Container mydsl_container;




    private myDsl_Visualizer mydsl_visualizer;




    private myDsl_RouterComponent mydsl_routercomponent;


    public myDsl_AbstractFrontElement(
    ) {
    }



    public myDsl_ReactApp getMydsl_reactapp() {
        return mydsl_reactapp;
    }

    public void setMydsl_reactapp(myDsl_ReactApp mydsl_reactapp) {
        this.mydsl_reactapp = mydsl_reactapp;
    }
    public myDsl_Reducer getMydsl_reducer() {
        return mydsl_reducer;
    }

    public void setMydsl_reducer(myDsl_Reducer mydsl_reducer) {
        this.mydsl_reducer = mydsl_reducer;
    }
    public myDsl_Container getMydsl_container() {
        return mydsl_container;
    }

    public void setMydsl_container(myDsl_Container mydsl_container) {
        this.mydsl_container = mydsl_container;
    }
    public myDsl_Visualizer getMydsl_visualizer() {
        return mydsl_visualizer;
    }

    public void setMydsl_visualizer(myDsl_Visualizer mydsl_visualizer) {
        this.mydsl_visualizer = mydsl_visualizer;
    }
    public myDsl_RouterComponent getMydsl_routercomponent() {
        return mydsl_routercomponent;
    }

    public void setMydsl_routercomponent(myDsl_RouterComponent mydsl_routercomponent) {
        this.mydsl_routercomponent = mydsl_routercomponent;
    }

}