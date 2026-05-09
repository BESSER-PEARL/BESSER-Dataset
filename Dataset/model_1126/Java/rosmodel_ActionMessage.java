





import java.util.List;
import java.util.ArrayList;

public class rosmodel_ActionMessage  {

    private String name;





    private rosmodel_Package rosmodel_package;


    public rosmodel_ActionMessage(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rosmodel_Package getRosmodel_package() {
        return rosmodel_package;
    }

    public void setRosmodel_package(rosmodel_Package rosmodel_package) {
        this.rosmodel_package = rosmodel_package;
    }

}