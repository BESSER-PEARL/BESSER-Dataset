





import java.util.List;
import java.util.ArrayList;

public class myDsl_JsModule extends AbstractFrontElement {

    private String name;





    private myDsl_ReactApp mydsl_reactapp;




    private myDsl_ServiceFront mydsl_servicefront;




    private myDsl_Directory mydsl_directory;


    public myDsl_JsModule(
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

    public myDsl_ReactApp getMydsl_reactapp() {
        return mydsl_reactapp;
    }

    public void setMydsl_reactapp(myDsl_ReactApp mydsl_reactapp) {
        this.mydsl_reactapp = mydsl_reactapp;
    }
    public myDsl_ServiceFront getMydsl_servicefront() {
        return mydsl_servicefront;
    }

    public void setMydsl_servicefront(myDsl_ServiceFront mydsl_servicefront) {
        this.mydsl_servicefront = mydsl_servicefront;
    }
    public myDsl_Directory getMydsl_directory() {
        return mydsl_directory;
    }

    public void setMydsl_directory(myDsl_Directory mydsl_directory) {
        this.mydsl_directory = mydsl_directory;
    }

}