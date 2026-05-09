





import java.util.List;
import java.util.ArrayList;

public class research16_State extends StateMachineObject {

    private String kind;
    private int id;
    private String name;





    private research16_Paper research16_paper;


    public research16_State(
        String kind,        int id,        String name    ) {
        super(
        );
        this.kind = kind;
        this.id = id;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public research16_Paper getResearch16_paper() {
        return research16_paper;
    }

    public void setResearch16_paper(research16_Paper research16_paper) {
        this.research16_paper = research16_paper;
    }

}