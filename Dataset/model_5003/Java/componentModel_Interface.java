





import java.util.List;
import java.util.ArrayList;

public class componentModel_Interface  {

    private String name;





    private componentModel_Repository componentmodel_repository;


    public componentModel_Interface(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public componentModel_Repository getComponentmodel_repository() {
        return componentmodel_repository;
    }

    public void setComponentmodel_repository(componentModel_Repository componentmodel_repository) {
        this.componentmodel_repository = componentmodel_repository;
    }

}