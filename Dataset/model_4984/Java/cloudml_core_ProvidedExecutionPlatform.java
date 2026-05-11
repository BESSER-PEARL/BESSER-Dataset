





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ProvidedExecutionPlatform extends ExecutionPlatform {






    private List<Property> propertys;


    public cloudml_core_ProvidedExecutionPlatform(
    ) {
        super(
        );
        this.propertys = new ArrayList<>();
    }

    public cloudml_core_ProvidedExecutionPlatform(
        ArrayList<Property> propertys    ) {
        this.propertys = propertys;
    }


    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }

}