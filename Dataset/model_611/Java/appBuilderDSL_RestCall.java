





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_RestCall extends SetInstructionAssignment {

    private String url;



    public appBuilderDSL_RestCall(
        String url    ) {
        super(
        );
        this.url = url;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}