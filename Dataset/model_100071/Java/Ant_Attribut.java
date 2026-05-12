





import java.util.List;
import java.util.ArrayList;

public class Ant_Attribut  {

    private String value;
    private String name;





    private Ant_NewTask ant_newtask;


    public Ant_Attribut(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Ant_NewTask getAnt_newtask() {
        return ant_newtask;
    }

    public void setAnt_newtask(Ant_NewTask ant_newtask) {
        this.ant_newtask = ant_newtask;
    }

}