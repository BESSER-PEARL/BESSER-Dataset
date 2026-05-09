





import java.util.List;
import java.util.ArrayList;

public class dsl_ClassOrInterfaceDeclaration  {

    private String typeCategory;
    private String id;



    public dsl_ClassOrInterfaceDeclaration(
        String typeCategory,        String id    ) {
        this.typeCategory = typeCategory;
        this.id = id;
    }


    public String getTypecategory() {
        return typeCategory;
    }

    public void setTypecategory(String typeCategory) {
        this.typeCategory = typeCategory;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}