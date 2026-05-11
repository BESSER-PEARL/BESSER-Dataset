





import java.util.List;
import java.util.ArrayList;

public class smalluml_Methode  {

    private String name;
    private String returnType;





    private smalluml_SmallClass smalluml_smallclass;


    public smalluml_Methode(
        String name,        String returnType    ) {
        this.name = name;
        this.returnType = returnType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }

    public smalluml_SmallClass getSmalluml_smallclass() {
        return smalluml_smallclass;
    }

    public void setSmalluml_smallclass(smalluml_SmallClass smalluml_smallclass) {
        this.smalluml_smallclass = smalluml_smallclass;
    }

}