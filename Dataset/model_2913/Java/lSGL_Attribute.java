





import java.util.List;
import java.util.ArrayList;

public class lSGL_Attribute  {

    private boolean isMap;
    private boolean isList;
    private String name;
    private boolean isArray;





    private lSGL_Entity lsgl_entity;


    public lSGL_Attribute(
        boolean isMap,        boolean isList,        String name,        boolean isArray    ) {
        this.isMap = isMap;
        this.isList = isList;
        this.name = name;
        this.isArray = isArray;
    }


    public boolean getIsmap() {
        return isMap;
    }

    public void setIsmap(boolean isMap) {
        this.isMap = isMap;
    }
    public boolean getIslist() {
        return isList;
    }

    public void setIslist(boolean isList) {
        this.isList = isList;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsarray() {
        return isArray;
    }

    public void setIsarray(boolean isArray) {
        this.isArray = isArray;
    }

    public lSGL_Entity getLsgl_entity() {
        return lsgl_entity;
    }

    public void setLsgl_entity(lSGL_Entity lsgl_entity) {
        this.lsgl_entity = lsgl_entity;
    }

}