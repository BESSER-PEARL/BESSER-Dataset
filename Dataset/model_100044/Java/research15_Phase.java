





import java.util.List;
import java.util.ArrayList;

public class research15_Phase  {

    private String name;





    private research15_PublicationProcess research15_publicationprocess;


    public research15_Phase(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public research15_PublicationProcess getResearch15_publicationprocess() {
        return research15_publicationprocess;
    }

    public void setResearch15_publicationprocess(research15_PublicationProcess research15_publicationprocess) {
        this.research15_publicationprocess = research15_publicationprocess;
    }

}