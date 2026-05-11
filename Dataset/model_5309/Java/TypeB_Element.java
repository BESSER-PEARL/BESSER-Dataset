





import java.util.List;
import java.util.ArrayList;

public class TypeB_Element  {

    private String type;
    private String abstractBaseName;
    private String nameElement;



    public TypeB_Element(
        String type,        String abstractBaseName,        String nameElement    ) {
        this.type = type;
        this.abstractBaseName = abstractBaseName;
        this.nameElement = nameElement;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAbstractbasename() {
        return abstractBaseName;
    }

    public void setAbstractbasename(String abstractBaseName) {
        this.abstractBaseName = abstractBaseName;
    }
    public String getNameelement() {
        return nameElement;
    }

    public void setNameelement(String nameElement) {
        this.nameElement = nameElement;
    }


}