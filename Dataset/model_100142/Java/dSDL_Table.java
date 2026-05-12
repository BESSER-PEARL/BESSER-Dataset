





import java.util.List;
import java.util.ArrayList;

public class dSDL_Table  {

    private String name;





    private List<dSDL_Attribute> dsdl_attributes;




    private dSDL_Database dsdl_database;


    public dSDL_Table(
        String name    ) {
        this.name = name;
        this.dsdl_attributes = new ArrayList<>();
    }

    public dSDL_Table(
        String name        ArrayList<dSDL_Attribute> dsdl_attributes    ) {
        this.name = name;
        this.dsdl_attributes = dsdl_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<dSDL_Attribute> getDsdl_attributes() {
        return dsdl_attributes;
    }

    public void addDsdl_attribute(Dsdl_attribute dsdl_attribute) {
        this.dsdl_attributes.add(dsdl_attribute);
    }
    public dSDL_Database getDsdl_database() {
        return dsdl_database;
    }

    public void setDsdl_database(dSDL_Database dsdl_database) {
        this.dsdl_database = dsdl_database;
    }

}