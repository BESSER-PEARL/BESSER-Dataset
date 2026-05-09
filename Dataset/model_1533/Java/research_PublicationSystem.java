





import java.util.List;
import java.util.ArrayList;

public class research_PublicationSystem extends Named {






    private research_PublicationProcess research_publicationprocess;




    private research_PublicationStructure research_publicationstructure;


    public research_PublicationSystem(
    ) {
        super(
        );
    }



    public research_PublicationProcess getResearch_publicationprocess() {
        return research_publicationprocess;
    }

    public void setResearch_publicationprocess(research_PublicationProcess research_publicationprocess) {
        this.research_publicationprocess = research_publicationprocess;
    }
    public research_PublicationStructure getResearch_publicationstructure() {
        return research_publicationstructure;
    }

    public void setResearch_publicationstructure(research_PublicationStructure research_publicationstructure) {
        this.research_publicationstructure = research_publicationstructure;
    }

}