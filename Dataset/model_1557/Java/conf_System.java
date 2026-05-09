





import java.util.List;
import java.util.ArrayList;

public class conf_System  {






    private List<conf_Laboratory> conf_laboratorys;


    public conf_System(
    ) {
        this.conf_laboratorys = new ArrayList<>();
    }

    public conf_System(
        ArrayList<conf_Laboratory> conf_laboratorys    ) {
        this.conf_laboratorys = conf_laboratorys;
    }


    public List<conf_Laboratory> getConf_laboratorys() {
        return conf_laboratorys;
    }

    public void addConf_laboratory(Conf_laboratory conf_laboratory) {
        this.conf_laboratorys.add(conf_laboratory);
    }

}