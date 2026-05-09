





import java.util.List;
import java.util.ArrayList;

public class myDsl_RouterComponent extends UIComponent, AbstractFrontElement {

    private String name;





    private myDsl_Functionality mydsl_functionality;


    public myDsl_RouterComponent(
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

    public myDsl_Functionality getMydsl_functionality() {
        return mydsl_functionality;
    }

    public void setMydsl_functionality(myDsl_Functionality mydsl_functionality) {
        this.mydsl_functionality = mydsl_functionality;
    }

}