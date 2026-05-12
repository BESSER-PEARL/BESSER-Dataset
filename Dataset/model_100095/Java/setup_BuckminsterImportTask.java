





import java.util.List;
import java.util.ArrayList;

public class setup_BuckminsterImportTask extends BasicMaterializationTask {

    private String mspec;



    public setup_BuckminsterImportTask(
        String mspec    ) {
        super(
        );
        this.mspec = mspec;
    }


    public String getMspec() {
        return mspec;
    }

    public void setMspec(String mspec) {
        this.mspec = mspec;
    }


}