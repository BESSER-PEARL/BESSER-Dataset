





import java.util.List;
import java.util.ArrayList;

public class conts_G extends Named {






    private conts_B conts_b;




    private List<conts_H> conts_hs;


    public conts_G(
    ) {
        super(
        );
        this.conts_hs = new ArrayList<>();
    }

    public conts_G(
        ArrayList<conts_H> conts_hs    ) {
        this.conts_hs = conts_hs;
    }


    public conts_B getConts_b() {
        return conts_b;
    }

    public void setConts_b(conts_B conts_b) {
        this.conts_b = conts_b;
    }
    public List<conts_H> getConts_hs() {
        return conts_hs;
    }

    public void addConts_h(Conts_h conts_h) {
        this.conts_hs.add(conts_h);
    }

}