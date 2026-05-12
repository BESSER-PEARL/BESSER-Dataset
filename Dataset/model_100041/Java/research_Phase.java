





import java.util.List;
import java.util.ArrayList;

public class research_Phase  {

    private String name;





    private research_PublicationProcess research_publicationprocess;


    public research_Phase(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public research_PublicationProcess getResearch_publicationprocess() {
        return research_publicationprocess;
    }

    public void setResearch_publicationprocess(research_PublicationProcess research_publicationprocess) {
        this.research_publicationprocess = research_publicationprocess;
    }

}