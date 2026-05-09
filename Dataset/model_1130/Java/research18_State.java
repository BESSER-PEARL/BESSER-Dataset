





import java.util.List;
import java.util.ArrayList;

public class research18_State extends StateMachineObject {

    private String name;
    private String kind;
    private int id;





    private research18_Paper research18_paper;


    public research18_State(
        String name,        String kind,        int id    ) {
        super(
        );
        this.name = name;
        this.kind = kind;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public research18_Paper getResearch18_paper() {
        return research18_paper;
    }

    public void setResearch18_paper(research18_Paper research18_paper) {
        this.research18_paper = research18_paper;
    }

}