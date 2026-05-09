





import java.util.List;
import java.util.ArrayList;

public class research32_State extends StateMachineObject {

    private int id;
    private String name;
    private String kind;





    private research32_PublicationStatus research32_publicationstatus;




    private research32_Paper research32_paper;


    public research32_State(
        int id,        String name,        String kind    ) {
        super(
        );
        this.id = id;
        this.name = name;
        this.kind = kind;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public research32_PublicationStatus getResearch32_publicationstatus() {
        return research32_publicationstatus;
    }

    public void setResearch32_publicationstatus(research32_PublicationStatus research32_publicationstatus) {
        this.research32_publicationstatus = research32_publicationstatus;
    }
    public research32_Paper getResearch32_paper() {
        return research32_paper;
    }

    public void setResearch32_paper(research32_Paper research32_paper) {
        this.research32_paper = research32_paper;
    }

}