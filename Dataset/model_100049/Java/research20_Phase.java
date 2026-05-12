





import java.util.List;
import java.util.ArrayList;

public class research20_Phase  {

    private String name;





    private research20_PublicationProcess research20_publicationprocess;


    public research20_Phase(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public research20_PublicationProcess getResearch20_publicationprocess() {
        return research20_publicationprocess;
    }

    public void setResearch20_publicationprocess(research20_PublicationProcess research20_publicationprocess) {
        this.research20_publicationprocess = research20_publicationprocess;
    }

}