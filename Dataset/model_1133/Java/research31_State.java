





import java.util.List;
import java.util.ArrayList;

public class research31_State extends StateMachineObject {

    private int id;
    private String kind;
    private String name;





    private research31_Paper research31_paper;


    public research31_State(
        int id,        String kind,        String name    ) {
        super(
        );
        this.id = id;
        this.kind = kind;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public research31_Paper getResearch31_paper() {
        return research31_paper;
    }

    public void setResearch31_paper(research31_Paper research31_paper) {
        this.research31_paper = research31_paper;
    }

}