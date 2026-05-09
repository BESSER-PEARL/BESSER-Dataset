





import java.util.List;
import java.util.ArrayList;

public class mvc_Attribute  {

    private String nameattribute;
    private String typeattribute;



    public mvc_Attribute(
        String nameattribute,        String typeattribute    ) {
        this.nameattribute = nameattribute;
        this.typeattribute = typeattribute;
    }


    public String getNameattribute() {
        return nameattribute;
    }

    public void setNameattribute(String nameattribute) {
        this.nameattribute = nameattribute;
    }
    public String getTypeattribute() {
        return typeattribute;
    }

    public void setTypeattribute(String typeattribute) {
        this.typeattribute = typeattribute;
    }


}