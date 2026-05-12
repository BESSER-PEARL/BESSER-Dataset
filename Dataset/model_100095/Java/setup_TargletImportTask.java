





import java.util.List;
import java.util.ArrayList;

public class setup_TargletImportTask extends SetupTask {

    private String targletURI;



    public setup_TargletImportTask(
        String targletURI    ) {
        super(
        );
        this.targletURI = targletURI;
    }


    public String getTargleturi() {
        return targletURI;
    }

    public void setTargleturi(String targletURI) {
        this.targletURI = targletURI;
    }


}