





import java.util.List;
import java.util.ArrayList;

public class remes_Mode extends ControlPath {

    private String initialization;





    private remes_RemesDiagram remes_remesdiagram;


    public remes_Mode(
        String initialization    ) {
        super(
        );
        this.initialization = initialization;
    }


    public String getInitialization() {
        return initialization;
    }

    public void setInitialization(String initialization) {
        this.initialization = initialization;
    }

    public remes_RemesDiagram getRemes_remesdiagram() {
        return remes_remesdiagram;
    }

    public void setRemes_remesdiagram(remes_RemesDiagram remes_remesdiagram) {
        this.remes_remesdiagram = remes_remesdiagram;
    }

}