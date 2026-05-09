





import java.util.List;
import java.util.ArrayList;

public class myDsl_LogicContent  {

    private String name;





    private myDsl_ComponentsLogic mydsl_componentslogic;


    public myDsl_LogicContent(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_ComponentsLogic getMydsl_componentslogic() {
        return mydsl_componentslogic;
    }

    public void setMydsl_componentslogic(myDsl_ComponentsLogic mydsl_componentslogic) {
        this.mydsl_componentslogic = mydsl_componentslogic;
    }

}