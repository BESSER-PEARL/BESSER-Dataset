





import java.util.List;
import java.util.ArrayList;

public class research23_State extends StateMachineObject {

    private String name;
    private int id;
    private String kind;





    private research23_Paper research23_paper;


    public research23_State(
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

    public research23_Paper getResearch23_paper() {
        return research23_paper;
    }

    public void setResearch23_paper(research23_Paper research23_paper) {
        this.research23_paper = research23_paper;
    }

}