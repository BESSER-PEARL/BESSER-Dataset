





import java.util.List;
import java.util.ArrayList;

public class Docbook_ExampleType  {

    private String id;





    private Docbook_TitleType docbook_titletype;




    private Docbook_ProgramlistingType docbook_programlistingtype;




    private Docbook_SectionType docbook_sectiontype;


    public Docbook_ExampleType(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Docbook_TitleType getDocbook_titletype() {
        return docbook_titletype;
    }

    public void setDocbook_titletype(Docbook_TitleType docbook_titletype) {
        this.docbook_titletype = docbook_titletype;
    }
    public Docbook_ProgramlistingType getDocbook_programlistingtype() {
        return docbook_programlistingtype;
    }

    public void setDocbook_programlistingtype(Docbook_ProgramlistingType docbook_programlistingtype) {
        this.docbook_programlistingtype = docbook_programlistingtype;
    }
    public Docbook_SectionType getDocbook_sectiontype() {
        return docbook_sectiontype;
    }

    public void setDocbook_sectiontype(Docbook_SectionType docbook_sectiontype) {
        this.docbook_sectiontype = docbook_sectiontype;
    }

}