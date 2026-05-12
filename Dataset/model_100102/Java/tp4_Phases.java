





import java.util.List;
import java.util.ArrayList;

public class tp4_Phases  {

    private String name;





    private tp4_PublicationProcess tp4_publicationprocess;


    public tp4_Phases(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tp4_PublicationProcess getTp4_publicationprocess() {
        return tp4_publicationprocess;
    }

    public void setTp4_publicationprocess(tp4_PublicationProcess tp4_publicationprocess) {
        this.tp4_publicationprocess = tp4_publicationprocess;
    }

}