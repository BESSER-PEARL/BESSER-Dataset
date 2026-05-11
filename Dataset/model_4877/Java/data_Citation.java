





import java.util.List;
import java.util.ArrayList;

public class data_Citation extends MetaInformation {

    private String citationData;



    public data_Citation(
        String citationData    ) {
        super(
        );
        this.citationData = citationData;
    }


    public String getCitationdata() {
        return citationData;
    }

    public void setCitationdata(String citationData) {
        this.citationData = citationData;
    }


}