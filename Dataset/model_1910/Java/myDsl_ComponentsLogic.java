





import java.util.List;
import java.util.ArrayList;

public class myDsl_ComponentsLogic  {

    private String name;





    private myDsl_ReactComponents mydsl_reactcomponents;


    public myDsl_ComponentsLogic(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_ReactComponents getMydsl_reactcomponents() {
        return mydsl_reactcomponents;
    }

    public void setMydsl_reactcomponents(myDsl_ReactComponents mydsl_reactcomponents) {
        this.mydsl_reactcomponents = mydsl_reactcomponents;
    }

}