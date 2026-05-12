





import java.util.List;
import java.util.ArrayList;

public class research2_Phase  {

    private String name;





    private research2_PublicationProcess research2_publicationprocess;


    public research2_Phase(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public research2_PublicationProcess getResearch2_publicationprocess() {
        return research2_publicationprocess;
    }

    public void setResearch2_publicationprocess(research2_PublicationProcess research2_publicationprocess) {
        this.research2_publicationprocess = research2_publicationprocess;
    }

}