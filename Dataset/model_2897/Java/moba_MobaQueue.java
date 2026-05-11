





import java.util.List;
import java.util.ArrayList;

public class moba_MobaQueue extends MobaData {

    private String name;





    private moba_MobaQueue moba_mobaqueue;




    private moba_MobaCache moba_mobacache;


    public moba_MobaQueue(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public moba_MobaQueue getMoba_mobaqueue() {
        return moba_mobaqueue;
    }

    public void setMoba_mobaqueue(moba_MobaQueue moba_mobaqueue) {
        this.moba_mobaqueue = moba_mobaqueue;
    }
    public moba_MobaCache getMoba_mobacache() {
        return moba_mobacache;
    }

    public void setMoba_mobacache(moba_MobaCache moba_mobacache) {
        this.moba_mobacache = moba_mobacache;
    }

}