





import java.util.List;
import java.util.ArrayList;

public class research19_State extends StateMachineObject {

    private String name;
    private String kind;
    private int id;





    private research19_Paper research19_paper;


    public research19_State(
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

    public research19_Paper getResearch19_paper() {
        return research19_paper;
    }

    public void setResearch19_paper(research19_Paper research19_paper) {
        this.research19_paper = research19_paper;
    }

}