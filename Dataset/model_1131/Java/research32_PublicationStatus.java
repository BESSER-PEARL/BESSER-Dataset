





import java.util.List;
import java.util.ArrayList;

public class research32_PublicationStatus  {

    private String label;





    private research32_PublicationStructure research32_publicationstructure;


    public research32_PublicationStatus(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public research32_PublicationStructure getResearch32_publicationstructure() {
        return research32_publicationstructure;
    }

    public void setResearch32_publicationstructure(research32_PublicationStructure research32_publicationstructure) {
        this.research32_publicationstructure = research32_publicationstructure;
    }

}