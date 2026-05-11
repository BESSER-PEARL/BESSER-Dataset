





import java.util.List;
import java.util.ArrayList;

public class test_PatchTestModel  {

    private String oneAttribute;
    private String id;
    private String multiAttribute;



    public test_PatchTestModel(
        String oneAttribute,        String id,        String multiAttribute    ) {
        this.oneAttribute = oneAttribute;
        this.id = id;
        this.multiAttribute = multiAttribute;
    }


    public String getOneattribute() {
        return oneAttribute;
    }

    public void setOneattribute(String oneAttribute) {
        this.oneAttribute = oneAttribute;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getMultiattribute() {
        return multiAttribute;
    }

    public void setMultiattribute(String multiAttribute) {
        this.multiAttribute = multiAttribute;
    }


}