





import java.util.List;
import java.util.ArrayList;

public class SPL_Declaration extends LocatedElement {

    private String name;





    private SPL_Service spl_service;


    public SPL_Declaration(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SPL_Service getSpl_service() {
        return spl_service;
    }

    public void setSpl_service(SPL_Service spl_service) {
        this.spl_service = spl_service;
    }

}