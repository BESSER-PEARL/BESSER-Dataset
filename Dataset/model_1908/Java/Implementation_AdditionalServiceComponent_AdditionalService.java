





import java.util.List;
import java.util.ArrayList;

public class Implementation_AdditionalServiceComponent_AdditionalService  {

    private String description;
    private String name;
    private String price;
    private String usable;





    private Implementation_AdditionalServiceComponent_AdditionalServiceHandler implementation_additionalservicecomponent_additionalservicehandler;


    public Implementation_AdditionalServiceComponent_AdditionalService(
        String description,        String name,        String price,        String usable    ) {
        this.description = description;
        this.name = name;
        this.price = price;
        this.usable = usable;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getUsable() {
        return usable;
    }

    public void setUsable(String usable) {
        this.usable = usable;
    }

    public Implementation_AdditionalServiceComponent_AdditionalServiceHandler getImplementation_additionalservicecomponent_additionalservicehandler() {
        return implementation_additionalservicecomponent_additionalservicehandler;
    }

    public void setImplementation_additionalservicecomponent_additionalservicehandler(Implementation_AdditionalServiceComponent_AdditionalServiceHandler implementation_additionalservicecomponent_additionalservicehandler) {
        this.implementation_additionalservicecomponent_additionalservicehandler = implementation_additionalservicecomponent_additionalservicehandler;
    }

}