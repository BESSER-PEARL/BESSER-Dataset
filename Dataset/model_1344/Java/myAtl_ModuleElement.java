





import java.util.List;
import java.util.ArrayList;

public class myAtl_ModuleElement  {

    private String name;





    private myAtl_Module myatl_module;


    public myAtl_ModuleElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myAtl_Module getMyatl_module() {
        return myatl_module;
    }

    public void setMyatl_module(myAtl_Module myatl_module) {
        this.myatl_module = myatl_module;
    }

}