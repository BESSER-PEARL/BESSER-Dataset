





import java.util.List;
import java.util.ArrayList;

public class research18_State extends StateMachineObject {

    private String name;
    private int id;
    private String kind;





    private research18_Paper research18_paper;


    public research18_State(
        String name,        int id,        String kind    ) {
        super(
        );
        this.name = name;
        this.id = id;
        this.kind = kind;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public research18_Paper getResearch18_paper() {
        return research18_paper;
    }

    public void setResearch18_paper(research18_Paper research18_paper) {
        this.research18_paper = research18_paper;
    }

}