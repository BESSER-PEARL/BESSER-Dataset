





import java.util.List;
import java.util.ArrayList;

public class nabla_ItemType  {

    private String name;





    private nabla_NablaModule nabla_nablamodule;


    public nabla_ItemType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nabla_NablaModule getNabla_nablamodule() {
        return nabla_nablamodule;
    }

    public void setNabla_nablamodule(nabla_NablaModule nabla_nablamodule) {
        this.nabla_nablamodule = nabla_nablamodule;
    }

}