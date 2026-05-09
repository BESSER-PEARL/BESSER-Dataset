





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_NamedElement  {

    private String name;





    private umlclassdiagram_Feature umlclassdiagram_feature;


    public umlclassdiagram_NamedElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public umlclassdiagram_Feature getUmlclassdiagram_feature() {
        return umlclassdiagram_feature;
    }

    public void setUmlclassdiagram_feature(umlclassdiagram_Feature umlclassdiagram_feature) {
        this.umlclassdiagram_feature = umlclassdiagram_feature;
    }

}