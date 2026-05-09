





import java.util.List;
import java.util.ArrayList;

public class writers_Writer  {

    private String name;





    private writers_Catalog writers_catalog;


    public writers_Writer(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public writers_Catalog getWriters_catalog() {
        return writers_catalog;
    }

    public void setWriters_catalog(writers_Catalog writers_catalog) {
        this.writers_catalog = writers_catalog;
    }

}