





import java.util.List;
import java.util.ArrayList;

public class adb_ComponentChoiceList  {

    private String componentSelectorName;
    private boolean others;



    public adb_ComponentChoiceList(
        String componentSelectorName,        boolean others    ) {
        this.componentSelectorName = componentSelectorName;
        this.others = others;
    }


    public String getComponentselectorname() {
        return componentSelectorName;
    }

    public void setComponentselectorname(String componentSelectorName) {
        this.componentSelectorName = componentSelectorName;
    }
    public boolean getOthers() {
        return others;
    }

    public void setOthers(boolean others) {
        this.others = others;
    }


}