





import java.util.List;
import java.util.ArrayList;

public class vcml_PartialKey  {

    private String key;





    private vcml_Material vcml_material;




    private vcml_ObjectType vcml_objecttype;


    public vcml_PartialKey(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public vcml_Material getVcml_material() {
        return vcml_material;
    }

    public void setVcml_material(vcml_Material vcml_material) {
        this.vcml_material = vcml_material;
    }
    public vcml_ObjectType getVcml_objecttype() {
        return vcml_objecttype;
    }

    public void setVcml_objecttype(vcml_ObjectType vcml_objecttype) {
        this.vcml_objecttype = vcml_objecttype;
    }

}