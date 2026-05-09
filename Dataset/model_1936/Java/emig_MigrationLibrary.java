





import java.util.List;
import java.util.ArrayList;

public class emig_MigrationLibrary  {

    private String title;





    private emig_MyModel emig_mymodel;


    public emig_MigrationLibrary(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public emig_MyModel getEmig_mymodel() {
        return emig_mymodel;
    }

    public void setEmig_mymodel(emig_MyModel emig_mymodel) {
        this.emig_mymodel = emig_mymodel;
    }

}