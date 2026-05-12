





import java.util.List;
import java.util.ArrayList;

public class research31_State extends StateMachineObject {

    private int id;
    private String name;
    private String kind;



    public research31_State(
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


}