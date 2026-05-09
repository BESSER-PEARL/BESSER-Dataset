





import java.util.List;
import java.util.ArrayList;

public class dsl_Directory extends AbstractFrontElement {

    private String purpose;
    private String name;





    private dsl_Directory dsl_directory;


    public dsl_Directory(
        String purpose,        String name    ) {
        super(
        );
        this.purpose = purpose;
        this.name = name;
    }


    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Directory getDsl_directory() {
        return dsl_directory;
    }

    public void setDsl_directory(dsl_Directory dsl_directory) {
        this.dsl_directory = dsl_directory;
    }

}