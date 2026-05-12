





import java.util.List;
import java.util.ArrayList;

public class research23_State extends StateMachineObject {

    private int id;
    private String kind;
    private String name;





    private research23_Paper research23_paper;


    public research23_State(
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

    public research23_Paper getResearch23_paper() {
        return research23_paper;
    }

    public void setResearch23_paper(research23_Paper research23_paper) {
        this.research23_paper = research23_paper;
    }

}