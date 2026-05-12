





import java.util.List;
import java.util.ArrayList;

public class research20_State extends StateMachineObject {

    private int id;
    private String kind;
    private String name;





    private research20_Paper research20_paper;


    public research20_State(
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

    public research20_Paper getResearch20_paper() {
        return research20_paper;
    }

    public void setResearch20_paper(research20_Paper research20_paper) {
        this.research20_paper = research20_paper;
    }

}