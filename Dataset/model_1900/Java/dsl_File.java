





import java.util.List;
import java.util.ArrayList;

public class dsl_File extends AbstractFrontElement {

    private String name;
    private String type;





    private dsl_Directory dsl_directory;


    public dsl_File(
        String name,        String type    ) {
        super(
        );
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public dsl_Directory getDsl_directory() {
        return dsl_directory;
    }

    public void setDsl_directory(dsl_Directory dsl_directory) {
        this.dsl_directory = dsl_directory;
    }

}