





import java.util.List;
import java.util.ArrayList;

public class RandL_ServiceLevel  {

    private String name;





    private RandL_Container_RandL randl_container_randl;


    public RandL_ServiceLevel(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RandL_Container_RandL getRandl_container_randl() {
        return randl_container_randl;
    }

    public void setRandl_container_randl(RandL_Container_RandL randl_container_randl) {
        this.randl_container_randl = randl_container_randl;
    }

}