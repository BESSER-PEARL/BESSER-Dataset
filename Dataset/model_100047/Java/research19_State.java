





import java.util.List;
import java.util.ArrayList;

public class research19_State extends StateMachineObject {

    private String kind;
    private String name;
    private int id;





    private research19_Paper research19_paper;


    public research19_State(
        String kind,        String name,        int id    ) {
        super(
        );
        this.kind = kind;
        this.name = name;
        this.id = id;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
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

    public research19_Paper getResearch19_paper() {
        return research19_paper;
    }

    public void setResearch19_paper(research19_Paper research19_paper) {
        this.research19_paper = research19_paper;
    }

}