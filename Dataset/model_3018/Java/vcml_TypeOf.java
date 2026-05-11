





import java.util.List;
import java.util.ArrayList;

public class vcml_TypeOf extends Condition {

    private String location;





    private vcml_ObjectType vcml_objecttype;


    public vcml_TypeOf(
        String location    ) {
        super(
        );
        this.location = location;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public vcml_ObjectType getVcml_objecttype() {
        return vcml_objecttype;
    }

    public void setVcml_objecttype(vcml_ObjectType vcml_objecttype) {
        this.vcml_objecttype = vcml_objecttype;
    }

}