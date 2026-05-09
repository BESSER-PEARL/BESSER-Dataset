





import java.util.List;
import java.util.ArrayList;

public class research101_Phase  {

    private String name;





    private research101_PublicationProcess research101_publicationprocess;


    public research101_Phase(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public research101_PublicationProcess getResearch101_publicationprocess() {
        return research101_publicationprocess;
    }

    public void setResearch101_publicationprocess(research101_PublicationProcess research101_publicationprocess) {
        this.research101_publicationprocess = research101_publicationprocess;
    }

}