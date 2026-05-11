





import java.util.List;
import java.util.ArrayList;

public class base_PropertyTrace extends IdElement {

    private String name;





    private base_ModelElementTrace base_modelelementtrace;




    private base_PropertyAccess base_propertyaccess;


    public base_PropertyTrace(
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
    public base_PropertyAccess getBase_propertyaccess() {
        return base_propertyaccess;
    }

    public void setBase_propertyaccess(base_PropertyAccess base_propertyaccess) {
        this.base_propertyaccess = base_propertyaccess;
    }

}