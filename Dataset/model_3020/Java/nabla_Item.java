





import java.util.List;
import java.util.ArrayList;

public class nabla_Item  {

    private String name;





    private nabla_ItemDefinition nabla_itemdefinition;


    public nabla_Item(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nabla_ItemDefinition getNabla_itemdefinition() {
        return nabla_itemdefinition;
    }

    public void setNabla_itemdefinition(nabla_ItemDefinition nabla_itemdefinition) {
        this.nabla_itemdefinition = nabla_itemdefinition;
    }

}