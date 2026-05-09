





import java.util.List;
import java.util.ArrayList;

public class myDsl_Functionality extends AbstractFrontElement {

    private String name;





    private myDsl_State mydsl_state;




    private myDsl_ReactApp mydsl_reactapp;




    private myDsl_Container mydsl_container;




    private myDsl_ServiceFront mydsl_servicefront;




    private myDsl_Visualizer mydsl_visualizer;


    public myDsl_Functionality(
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

    public myDsl_State getMydsl_state() {
        return mydsl_state;
    }

    public void setMydsl_state(myDsl_State mydsl_state) {
        this.mydsl_state = mydsl_state;
    }
    public myDsl_ReactApp getMydsl_reactapp() {
        return mydsl_reactapp;
    }

    public void setMydsl_reactapp(myDsl_ReactApp mydsl_reactapp) {
        this.mydsl_reactapp = mydsl_reactapp;
    }
    public myDsl_Container getMydsl_container() {
        return mydsl_container;
    }

    public void setMydsl_container(myDsl_Container mydsl_container) {
        this.mydsl_container = mydsl_container;
    }
    public myDsl_ServiceFront getMydsl_servicefront() {
        return mydsl_servicefront;
    }

    public void setMydsl_servicefront(myDsl_ServiceFront mydsl_servicefront) {
        this.mydsl_servicefront = mydsl_servicefront;
    }
    public myDsl_Visualizer getMydsl_visualizer() {
        return mydsl_visualizer;
    }

    public void setMydsl_visualizer(myDsl_Visualizer mydsl_visualizer) {
        this.mydsl_visualizer = mydsl_visualizer;
    }

}