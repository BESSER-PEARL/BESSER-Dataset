





import java.util.List;
import java.util.ArrayList;

public class base_ModelTrace extends IdElement {

    private String name;





    private base_ModelElementTrace base_modelelementtrace;




    private base_ModelTypeTrace base_modeltypetrace;


    public base_ModelTrace(
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

    public base_ModelElementTrace getBase_modelelementtrace() {
        return base_modelelementtrace;
    }

    public void setBase_modelelementtrace(base_ModelElementTrace base_modelelementtrace) {
        this.base_modelelementtrace = base_modelelementtrace;
    }
    public base_ModelTypeTrace getBase_modeltypetrace() {
        return base_modeltypetrace;
    }

    public void setBase_modeltypetrace(base_ModelTypeTrace base_modeltypetrace) {
        this.base_modeltypetrace = base_modeltypetrace;
    }

}