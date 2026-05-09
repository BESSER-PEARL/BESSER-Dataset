





import java.util.List;
import java.util.ArrayList;

public class emig_MigrationLibrary  {

    private String name;





    private emig_MyModel emig_mymodel;


    public emig_MigrationLibrary(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public emig_MyModel getEmig_mymodel() {
        return emig_mymodel;
    }

    public void setEmig_mymodel(emig_MyModel emig_mymodel) {
        this.emig_mymodel = emig_mymodel;
    }

}